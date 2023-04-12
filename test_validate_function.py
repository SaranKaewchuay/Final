from function import validate_input
import pytest

# @pytest.mark.display
@pytest.mark.parametrize("workdays, total_ot_hours, num_late_days,expected_result", 
[
 (30, 3, 5, True),
 (28,4,1,"Number of OT hours must be a non-negative integer between 0 and 3."),
 (28,2,29,"Number of days late must be an integer between 0 and the number of workdays."),
 (-28.5,-2.5,-1.5,"Please provide non-negative numeric input only.")
])

def test_display(workdays, total_ot_hours, num_late_days,expected_result):
    actual_result = validate_input(workdays, total_ot_hours, num_late_days)
    assert expected_result == actual_result


