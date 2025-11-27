'''
Payment calculator 
Author: Zaw Min Tun
Description:
    This program will calculate the take-home income based on two inputs: Total worked hours and pay rate
'''

#Function to calculate gross pay
def calculate_gross_pay(hours_worked, pay_rate):
    return hours_worked * pay_rate


#Function to calculate tax
#Reference: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals
def calculate_tax(gross_pay):
    tax_rate = {
        15600: 0.105, #For each dollar of income 0 - $15600, tax rate 10.5%
        53500: 0.175, #For each dollar of income $15601 - $53500, tax rate 17.5%
        78100: 0.30, #For each dollar of income $53501 - $78100, tax rate 30%
        180000: 0.33, #For each dollar of income $78101 - $180000, tax rate 33%
        float("inf"): 0.39 #For each dollar of income $180001 and over, tax rate 39%
    }
    tax_resulted = 0
    already_taxed = 0
    for threshold, rate in tax_rate.items():
        if gross_pay > already_taxed:
            tax_resulted = tax_resulted + ((min(gross_pay, threshold) - already_taxed) * rate)
            #print(f"Tax up to {threshold}: {tax_resulted}") #Tracing the partial taxes
            already_taxed = threshold
        else:
            break
    return tax_resulted


#Main function
def main():
    print("\nType in the correct numbers to use the application effectively.")
    print("\n==============================================================\n")
    hours_worked = input("Hours worked (E.g. 2.5): ") #Getting user input for number of hours worked
    hours_worked = float(hours_worked) #Casting the input to float type
    pay_rate = input("Hourly pay rate (E.g. 75): ") #Getting user input for pay rate
    pay_rate = float(pay_rate) #Casting the input to float type

    #Calculating gross pay & tax
    gross_pay = calculate_gross_pay(hours_worked, pay_rate)
    tax = calculate_tax(gross_pay)

    #Printing the outcome
    print(f"Gross pay: {gross_pay:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Take-home: {(gross_pay - tax):.2f}")


if __name__ == "__main__":
    main()