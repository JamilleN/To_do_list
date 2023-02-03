def error_msg(error_code = 1):
    match error_code:
        case 1:
            print("\n****Number is OUT OF RANGE, please try again.****\n")
        case 2:
            print("\n****Please enter a NUMBER, try again.****\n")