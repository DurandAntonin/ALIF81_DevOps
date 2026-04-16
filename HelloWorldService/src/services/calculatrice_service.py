def add(x: int, y: int) -> int:
    return x + y

def mult(x: int, y: int) -> int:
    return sum(x for _ in range(y))

def reduce(x: int, y: int) -> int:
    return x - y

def divide(x: int, y: int) -> float:
    if y == 0:
        raise ZeroDivisionError(f"Can't divide {x} by {y}")

    return x / y