time = 17

is_hungry = False
match time :
    case 9:
        print("breakfast")
    case 14 | 13:
        print("lunch")
    case 17 if is_hungry :
        print("snacks")
    case 20:
        print("dinner")
    case _:
        print("work!")