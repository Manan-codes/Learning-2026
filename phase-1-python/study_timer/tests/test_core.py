from study_timer import core

def test_greet_returns_string():
    result = core.func("Manan", 21)
    assert isinstance(result, str)

def test_greet_contains_name():
    result = core.func("Manan", 21)
    assert "Manan" in result

def test_addition_returns_int():
    result = core.addition(5,6)
    assert isinstance(result, int)

def test_addition_adds():
    result = core.addition(3,7)
    assert result == (3+7)


def test_division_returns_float():
    result = core.division(5,8)
    assert isinstance(result, float)

def test_division_returns_None():
    result = core.division(5,0)
    assert result is None