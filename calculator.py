from math import sin, cos, tan, asin, acos, atan, pi

def calculate(operation, value):
    try:
        if operation == "sin":
            return sin(value)
        elif operation == "cos":
            return cos(value)
        elif operation == "tg":
            return tan(value)
        elif operation == "ctg":
            return 1 / tan(value) if tan(value) != 0 else "Undefined"
        elif operation == "arcsin":
            return asin(value) if -1 <= value <= 1 else "Undefined"
        elif operation == "arccos":
            return acos(value) if -1 <= value <= 1 else "Undefined"
        elif operation == "arctg":
            return atan(value)
        elif operation == "arcctg":
            return pi / 2 - atan(value)
        else:
            raise ValueError("Unsupported operation")
    except Exception as e:
        return str(e)
