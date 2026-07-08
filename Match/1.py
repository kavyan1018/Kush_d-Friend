day = int(input("Enter the day of the week (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
        
    case _:
        print("Invalid day. Please enter a number between 1 and 7.")