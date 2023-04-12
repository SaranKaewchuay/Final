from function import salary_calculator
import pytest

# @pytest.mark.display
@pytest.mark.parametrize("workdays, total_ot_hours, num_late_days,expected_result", 
[
     (30, 3, 5, 10380)
])

def test_display(workdays, total_ot_hours, num_late_days,expected_result):
    actual_result = salary_calculator(workdays, total_ot_hours, num_late_days)
    assert expected_result == actual_result


