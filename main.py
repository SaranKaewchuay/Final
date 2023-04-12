from function import display_salary
workdays = (input("Number of working days: "))
total_ot_hours = (input("Input Total OT hours: "))
num_late_days = (input("Number of days late: "))

try:
    try:
        input_workdays = int(workdays)
        input_total_ot_hours = int(total_ot_hours)
        input_num_late_days = int(num_late_days)
    except:
        input_workdays = float(workdays)
        input_total_ot_hours = float(total_ot_hours)
        input_num_late_days = float(num_late_days)

except:
        input_workdays = str(workdays)
        input_total_ot_hours = str(total_ot_hours)
        input_num_late_days = str(num_late_days)
    

salary = display_salary(input_workdays, input_total_ot_hours,  input_num_late_days)

if(type(salary) == int):
    print("Your salary is", salary,"฿")
else:
    print("Invalid Input: ",salary)
    
    

