from app.WorkTimerMain import *
import pytest

# @pytest.mark.parametrize("keyboard_input, expected_result", [
#     (pytest, True),
#     (pytest, True),
#     (7, True),
#     ("*", True),
#     (0, True),
#     (False, True),
#     (pytest, False),
#     (pytest, False),
#     ]
#                          )
def test_start_program(keyboard_input, expected_result):
    WorkTimerMain.start_program(keyboard_input) == expected_result

test_start_program("b", "True")