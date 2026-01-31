from notification import EmailNotification, SMSNotification, PushNotification


def main():
    notification = None
    notification_type = input(
        "Enter notification type (email/sms/push): ").lower()
    if notification_type == "email":
        notification = EmailNotification()
    elif notification_type == "sms":
        notification = SMSNotification()
    elif notification_type == "push":
        notification = PushNotification()
    else:
        print("Invalid notification type")

    if notification is not None:
        notification.send("Hello! This is a Factory Pattern example.")

    # When we want to send many notifications, there will be a lot of if-else checking or we need to find another way to make it better - factory pattern takes care of this


if __name__ == "__main__":
    main()
