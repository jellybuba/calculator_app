def multiplication(x: float, y: float)-> float:
    try:
        return x * y
    except ValueError:
        print("invalid number")