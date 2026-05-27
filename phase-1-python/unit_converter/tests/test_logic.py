from unit_converter import logic

def test__temp_converter_return_type():
    """Tests return value is float"""
    result = logic.temp_converter(25.42, 1)
    assert isinstance(result, float)


def test_temp_converter_calc1():
    """Tests conversion Celsius -> Fahrenheit"""
    result = logic.temp_converter(25.42, 1)
    assert round(result,2) == 77.76


def test_temp_converter_calc2():
    """Tests conversion Fahrenheit -> Celsius"""
    result = logic.temp_converter(41.5, 2)
    assert round(result,2) == 5.28


def test_weight_converter_return():
    """Tests return value is float"""
    result = logic.weight_converter(44.0,1)
    assert isinstance(result, float)

def test_weight_converter_calc1():
    """Tests conversion Kgs -> Lbs"""
    result = logic.weight_converter(44.0,1)
    assert round(result,2) == 97.02 

def test_weight_converter_calc2():
    """Tests conversion Lbs -> Kgs"""
    result = logic.weight_converter(44.0,2)
    assert round(result,2) == 19.95











