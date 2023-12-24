def divide(a, b):
    try:
        int("This is not a number")  # CAUSES VALUE ERROR
        return a / b

    except ValueError as e:
        print("ValueError", e)
    except NameError as e:
        print("NameError", e)
    except Exception as e:  # should go last, or else other except blocks will be unreachable
        print("General", e)


divide(9, 0)
