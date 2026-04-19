def calculator():
    def add():
        a=int(input("enter the your first number:"))
        b=int(input("enter the secod number:"))
        return a+b
    def subb():
        a=int(input("enter the your first number:"))
        b=int(input("enter the secod number:"))
        return a-b
    def multi():
        a=int(input("enter the your first number:"))
        b=int(input("enter the secod number:"))
        return a*b
    def divi():
        a=int(input("enter the your first number:"))
        b=int(input("enter the secod number:"))
        return a/b
    print("START YOUR CALCULATION")
    print(" 1.Addition\n 2.subraction\n 3.multipication\n 4.division")
    n=int(input("enter your choice:"))
    match n:
        case 1:
            result=add()
            print("result:",result)
        case 2:
            result=subb()
            print("result:",result)
        case 3:
            result=multi()
            print("result:",result)
        case 4:
            result=divi()
            print("result:",result)
        case _:
            print("INVALID CHOICE")
calculator()

