def validate_input(workdays, total_ot_hours, num_late_days):
    if not all(isinstance(i, (int, float)) and i >= 0 for i in [workdays, total_ot_hours, num_late_days]):
        return "Please provide non-negative numeric input only."
    elif not 0 <= workdays <= 31:
        return "Number of workdays must be between 0 and 31."
    elif (total_ot_hours != int(total_ot_hours) or num_late_days != int(num_late_days)):
          return "Decimal input not allowed. Must integer input only."    
    elif not 0 <= total_ot_hours <= 3 or not isinstance(total_ot_hours, int):
        return "Number of OT hours must be a non-negative integer between 0 and 3."
    elif not isinstance(num_late_days, int) or not 0 <= num_late_days <= workdays:
        return "Number of days late must be an integer between 0 and the number of workdays."
    else:
        return True



def salary_calculator(workdays,total_ot_hours,num_late_days):
    base_salary = 340 * workdays
    ot_salary = total_ot_hours * 60
    diligence_bonus = 0 
    if num_late_days == 0 and workdays > 0:
        diligence_bonus = 1000
    total_salary = base_salary + ot_salary + diligence_bonus
    return total_salary


def display_salary(workdays,total_ot_hours,num_late_days):
    status = validate_input(workdays,total_ot_hours,num_late_days)
    if(status == True):
        return salary_calculator(workdays,total_ot_hours,num_late_days)
    else:
        return status
