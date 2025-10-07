def validate_input(value):
    assert str(value).isnumeric(), "Value is not a number"
    
def validate_b_not_zero(value):
    assert value == 0, "b is ZERO"