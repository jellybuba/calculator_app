def division(x: float, y: float)-> float:
    try:
        if (x == 0 or y == 0):
            raise ValueError
        return x / y
    except ValueError:
        print("invalid number for division")