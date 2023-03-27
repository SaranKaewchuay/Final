from function import display_salary
import pytest

# @pytest.mark.display
@pytest.mark.parametrize("workdays, total_ot_hours, num_late_days,expected_result", 
[(0, 0, 0, 0),(22, 0, 0,8480),(22, 3, 0,8660) ,(21, 0, 1,7140),(21, 2, 1,7260),
 (31, 0, 0,11540),(31, 3, 0,11720),(31,0,5,10540),(31,3,31,10720),
 (-5,-5,-5,"number of workdays or number of late days must be between 0 and 31"),
 (-5,2,3,"number of workdays or number of late days must be between 0 and 31"),
 (22.5,2,3,"input integer"),
 (22,2,3.5,"input integer"),
 (35,4,32,"number of workdays or number of late days must be between 0 and 31"),
 (35,4,10,"number of workdays or number of late days must be between 0 and 31"),
 (35,3,32,"number of workdays or number of late days must be between 0 and 31"),
 (22,4,32,"number of workdays or number of late days must be between 0 and 31"),
 (22,4,5,"total OT hours must be between 0 and 3"),
 (22,4,25,"number of late days. Not more than number of workdays"),
 (22,3,25,"number of late days. Not more than number of workdays"),
 ("a","a","a","input integer"),
 ("a",2,4,"input integer"),
 ("a",2,"a","input integer"),
])

def test_display(workdays, total_ot_hours, num_late_days,expected_result):
    actual_result = display_salary(workdays, total_ot_hours, num_late_days)
    assert expected_result == actual_result


