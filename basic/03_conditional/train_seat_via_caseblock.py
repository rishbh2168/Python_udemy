seat = input("please enter your seat (sleeper/ac/general/luxury) : ").lower()

match seat :
    case "sleeper":
        print("this is non ac")
    case "ac":
        print("this is have ac")
    case "general":
        print("this low class seat")
    case "luxury":
        print("this seat is vip seat with free food")
    case _ :
        print("invalid seat")
    