print("\nType in the correct numbers to use the application effectively.")
print("\n==============================================================\n")
HoursWorked = input("Hours worked (E.g. 2.5):")
HoursWorked = float(HoursWorked)
HourlyPayRate = input("Hourly pay rate (E.g. 75):")
HourlyPayRate = float(HourlyPayRate)
GrossPay = HoursWorked * HourlyPayRate
print(f"Gross pay: {GrossPay}")