from function import salary_calculator
import pytest

# @pytest.mark.display
@pytest.mark.parametrize("workdays, total_ot_hours, num_late_days,expected_result", 
[(0, 0, 0, 0),(22, 0, 0,8480),(22, 3, 0,8660) ,(21, 0, 1,7140),(21, 2, 1,7260),
 (31, 0, 0,11540),(31, 3, 0,11720),(31,0,5,10540),(31,3,31,10720),

])

def test_display(workdays, total_ot_hours, num_late_days,expected_result):
    actual_result = salary_calculator(workdays, total_ot_hours, num_late_days)
    assert expected_result == actual_result


