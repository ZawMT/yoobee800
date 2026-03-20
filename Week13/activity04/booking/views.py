import json
import uuid
from datetime import date, timedelta
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

AVAILABILITY_FILE = settings.DATA_DIR / 'availability.json'
BOOKING_FILE = settings.DATA_DIR / 'booking.json'

SLOT_TIMES = {
    1:  ("09:00", "09:30"),
    2:  ("09:30", "10:00"),
    3:  ("10:00", "10:30"),
    4:  ("10:30", "11:00"),
    5:  ("11:00", "11:30"),
    6:  ("11:30", "12:00"),
    7:  ("12:00", "12:30"),
    8:  ("12:30", "13:00"),
    9:  ("14:00", "14:30"),
    10: ("14:30", "15:00"),
    11: ("15:00", "15:30"),
    12: ("15:30", "16:00"),
    13: ("16:00", "16:30"),
    14: ("16:30", "17:00"),
}


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def get_week_dates(offset=0):
    today = date.today()
    monday = today - timedelta(days=today.weekday()) + timedelta(weeks=offset)
    return [monday + timedelta(days=i) for i in range(5)]  # Mon-Fri


def makebooking(request):
    availability = load_json(AVAILABILITY_FILE)
    teachers = [{"id": t["id"], "teacher_name": t["teacher_name"]} for t in availability]
    slot_times = {str(k): {"start": v[0], "end": v[1]} for k, v in SLOT_TIMES.items()}
    return render(request, 'booking/makebooking.html', {
        'teachers': json.dumps(teachers),
        'slot_times': json.dumps(slot_times),
    })


def bookinginfo(request):
    bookings = load_json(BOOKING_FILE)
    for b in bookings:
        slot = b.get('slot')
        if slot and slot in SLOT_TIMES:
            b['slot_start'] = SLOT_TIMES[slot][0]
            b['slot_end'] = SLOT_TIMES[slot][1]
    bookings.sort(key=lambda b: (b.get('date', ''), b.get('slot', 0)))
    return render(request, 'booking/bookinginfo.html', {'bookings': bookings})


def api_slots(request):
    teacher_id = request.GET.get('teacher_id')
    week_offset = int(request.GET.get('week_offset', 0))

    availability = load_json(AVAILABILITY_FILE)
    bookings = load_json(BOOKING_FILE)
    week_dates = get_week_dates(week_offset)

    teacher = next((t for t in availability if t['id'] == teacher_id), None)
    if not teacher:
        return JsonResponse({'error': 'Teacher not found'}, status=404)

    booked_slots = {}
    for b in bookings:
        if b['teacher_id'] == teacher_id:
            booked_slots.setdefault(b['date'], set()).add(b['slot'])

    result = []
    for d in week_dates:
        date_str = d.strftime('%Y-%m-%d')
        avail_entry = next((a for a in teacher['availability'] if a['date'] == date_str), None)
        available = avail_entry['slots'] if avail_entry else []
        already_booked = booked_slots.get(date_str, set())
        free_slots = [s for s in available if s not in already_booked]
        result.append({
            'date': date_str,
            'day_name': d.strftime('%A'),
            'slots': free_slots,
        })

    slot_times = {str(k): {"start": v[0], "end": v[1]} for k, v in SLOT_TIMES.items()}
    return JsonResponse({'week': result, 'slot_times': slot_times})


@csrf_exempt
@require_http_methods(["POST"])
def api_book(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    required = ['teacher_id', 'teacher_name', 'student_id', 'student_name', 'reason', 'date', 'slot']
    for field in required:
        if not data.get(field):
            return JsonResponse({'error': f'Missing field: {field}'}, status=400)

    availability = load_json(AVAILABILITY_FILE)
    bookings = load_json(BOOKING_FILE)

    teacher = next((t for t in availability if t['id'] == data['teacher_id']), None)
    if not teacher:
        return JsonResponse({'error': 'Teacher not found'}, status=404)

    avail_entry = next((a for a in teacher['availability'] if a['date'] == data['date']), None)
    if not avail_entry or data['slot'] not in avail_entry['slots']:
        return JsonResponse({'error': 'Slot not available'}, status=409)

    already_booked = any(
        b['teacher_id'] == data['teacher_id'] and
        b['date'] == data['date'] and
        b['slot'] == data['slot']
        for b in bookings
    )
    if already_booked:
        return JsonResponse({'error': 'Slot already booked'}, status=409)

    new_booking = {
        'id': str(uuid.uuid4()),
        'teacher_id': data['teacher_id'],
        'teacher_name': data['teacher_name'],
        'student_id': data['student_id'],
        'student_name': data['student_name'],
        'reason': data['reason'],
        'date': data['date'],
        'slot': data['slot'],
    }
    bookings.append(new_booking)
    save_json(BOOKING_FILE, bookings)

    avail_entry['slots'].remove(data['slot'])
    save_json(AVAILABILITY_FILE, availability)

    return JsonResponse({'success': True, 'booking_id': new_booking['id']})
