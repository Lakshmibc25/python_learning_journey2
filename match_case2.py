day = "sunday"

match day:
    case "monday":
        print("start of the work week.")
    case "friday":
        print("almost weekend!")
    case "saturday" | "sunday":
        print("its the weekend !")
    case _:
        print("just another weekday.")