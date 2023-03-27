# def validate_input(workdays, total_ot_hours, num_late_days):
#     try:
#         workdays = int(workdays)
#         total_ot_hours = int(total_ot_hours)
#         num_late_days = int(num_late_days)
#         if not 0 <= workdays <= 31 or not 0 <= num_late_days <= 31:
#             return "Invalid input: number of workdays or number of late days must be between 0 and 31"    
#         if num_late_days > workdays:
#             return "Invalid input: number of late days. Not more than number of workdays"
#         if not 0 <= total_ot_hours <= 3:
#             return "Invalid input: total OT hours must be between 0 and 3"
#     except ValueError:
#         return "Invalid input: input positive integers"
#     else:
#         return True


def validate_input(workdays, total_ot_hours, num_late_days):
    if (type(workdays) != int or type(total_ot_hours) != int or type(num_late_days) != int):
          if type(workdays) == str or type(total_ot_hours) == str or type(num_late_days) == str:
            return "input integer"
          elif workdays >= 1 and workdays <= 12 or total_ot_hours >= 1 and total_ot_hours <= 12 or num_late_days >= 1 and num_late_days <= 12:
            return "input integer"
          else:
            return "out of range must be between 0 and 31"
    elif (not 0 <= workdays <= 31 or not 0 <= num_late_days <= 31):
        return "number of workdays or number of late days must be between 0 and 31" 
    elif (num_late_days > workdays): 
        return "number of late days. Not more than number of workdays"
    elif not 0 <= total_ot_hours <= 3:
        return "total OT hours must be between 0 and 3"
    else:
        return True 

    
def salary_calculator(workdays,total_ot_hours,num_late_days):
    base_salary = 340 * workdays
    ot_salary = min(total_ot_hours, 3) * 60
    diligence_bonus = 0 if num_late_days > 0 else 1000
    total_salary = base_salary + ot_salary + diligence_bonus
    return total_salary



def display_salary(workdays,total_ot_hours,num_late_days):
    status = validate_input(workdays,total_ot_hours,num_late_days)
    if(status == True):
        return salary_calculator(workdays,total_ot_hours,num_late_days)
    else:
        return status
