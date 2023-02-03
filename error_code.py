#This file is a dir for error codes

def error_msg(error_code:int):
    """"Input a error code and print out 
    the corresponding error msg"""
    match error_code:
        case 1:
            print("\n****Number is OUT OF RANGE, please try again.****\n")
        case 2:
            print("\n****Please enter a NUMBER, try again.****\n")
        case 3:
            print("\n****Invalid COMMAND, please try again.****\n")