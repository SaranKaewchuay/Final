from function import display_salary
import pytest

@pytest.mark.display
@pytest.mark.parametrize("num_workdays, num_ot_hours, num_late_days,expected_result", 
[(1,"january"),(2,"february"),(3,"march"),(4,"april"),
 (5,"may"),(6,"june"),(7,"july"),(8,"august"),
 (9,"september"),(10,"october"),(11,"november"),(12,"december"),
 (0,"out of range"),(13,"out of range"),(-10,"out of range"),
 (22,"out of range"),(1.1,"input integer"),(13.1,"out of range"),
 ("a","input integer"),("#","input integer"),(0.5,"out of range"),
 (-1.5,"out of range"),(1.5,"input integer")
])

def test_display(num_workdays, num_ot_hours, num_late_days,expected_result):
    actual_result = display_salary(num_workdays, num_ot_hours, num_late_days)
    assert expected_result == actual_result


