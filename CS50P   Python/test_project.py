from project import *
from tud_test_base import set_keyboard_input, get_display_output



def test_get_true_input():
    set_keyboard_input(['r'])
    get_true_input(['r', 'p', 's'])
    output = get_display_output()
    assert output == ['Enter r p s: ']

def test_make_ai_choice():
    assert make_ai_choice(['r']) == 'r'
    assert make_ai_choice(['r', 'p']) == 'r' or 'p'
    assert make_ai_choice(['r', 'p' , 's']) == 'r' or 'p' or 's'


def test_comparator_user_to_ai_equal():
    assert comparator_user_to_ai('r', 'r') == 'Equal'

def test_comparator_user_to_ai_computer_won():
    assert comparator_user_to_ai('r', 'p') == 'Computer won'
