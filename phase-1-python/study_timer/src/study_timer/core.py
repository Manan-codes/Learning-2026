# Demo code for learning the project structures


def func(name: str, age: int) -> str:
    """Return greetings string with name and age"""
    return f"Hello {name}, you are {age} years old"

def addition(val1: int, val2: int) -> int:
    """Adds 2 integers and returns the result"""
    return val1 + val2

def division(val1: float, val2: float) -> None | float:
    """Takes in 2 float values and returns result by dividing 1st by 2nd or String if 2nd is 0"""
    if val2 == 0:
        return None
    return val1 / val2

if __name__ == "__main__":
    print(func("Raja", 21))
    print(addition(5,9))
    print(division(5.9,0))