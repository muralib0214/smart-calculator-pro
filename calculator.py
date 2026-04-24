def calculator():
    def input_number():
        # Use loop instead of recursion to handle invalid inputs
        # Recursion may cause stack overflow if user repeatedly enters invalid values
        while True:
            try:
                a=int(input("Enter the your first number:"))
                b=int(input("Enter the second number:"))
                return a,b
            except ValueError:  
                print("INVALID INPUT! Please enter numbers only.")
                
    def add():
        a,b=input_number()
        return a+b
    def subb():
        a,b=input_number()
        return a-b
    def multi():
        a,b=input_number()  
        return a*b
    def divi():
        a,b=input_number()
        try:
            return a/b
        except ZeroDivisionError:
            return("Error! Division by zero is not allowed.")
    def modulus():
        a,b=input_number()
        try:
            return a%b
        except ZeroDivisionError:
            return("Error! Modulus by zero is not allowed.")

    while True: 
        print("\n**********START YOUR CALCULATION***********")
        print(" 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Modulus\n 6.Exit")
        try:
            n=int(input("Enter your choice:"))
        except ValueError:
            print("INVALID INPUT! Please enter a valid option.")
            continue
        match n:
            case 1:
                print("result =",add())
            case 2:
                print("result =",subb())
            case 3:
                print("result =",multi())
            case 4:
                print("result =",divi())
            case 5:
                print("result =",modulus())
            case 6:
                print("Exiting the calculator...")
                break
            case _:
                print("INVALID CHOICE... Please select a valid option.")
calculator()

