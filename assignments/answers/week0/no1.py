name = input("Enter employee's name: ")
worked_hours = float(input("Enter number of hours worked in a week: "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))
federal_tax_rate = float(input("Enter federal tax withholding rate: "))
state_tax_rate = float(input("Enter state tax withholding rate: "))

gross_pay = worked_hours * hourly_pay_rate

federal_withholding = gross_pay * federal_tax_rate
state_withholding = gross_pay * state_tax_rate
total_deductions = federal_withholding + state_withholding
net_pay = gross_pay - total_deductions

print("Employee Name: ",name)
print("Hours Worked: ",format(worked_hours, ".1f"))
print("Pay Rate:$",format(hourly_pay_rate, ".2f"))
print("Gross Pay:$", format(gross_pay, ".2f"))
print("Deductions: ")
print("\tFederal Withholding (",format(federal_tax_rate * 100, ".2f"), "%): $",format(federal_withholding, ".2f"))
print("\tState Withholding (",format(state_tax_rate * 100, ".2f"), "%): $",format(state_withholding, ".2f"))
print("\tTotal Deduction:$",format(total_deductions, ".2f"))
print("Net Pay:$",format(net_pay, ".2f"))