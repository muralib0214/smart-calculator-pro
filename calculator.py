from datetime import datetime
def calculator():
    history_list = []  # List to store calculation history
    #hisrory file
    try:
        with open("history.txt", "r") as f: 
            history_list = f.read().splitlines()  
    except FileNotFoundError:
        pass
    #>>taking input from user and validating it
    def input_number():
        while True:
            try:
                a=float(input("Enter the first number:"))
                b=float(input("Enter the second number:"))
                return a,b
            except ValueError:  
                print("INVALID INPUT! Please enter numbers only.")
    #>>defining functions for each operation          
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def divi(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return("Error! Division by zero is not allowed.")
    def modulus(a,b):
        try:
            return a%b
        except ZeroDivisionError:
            return("Error! Modulus by zero is not allowed.")
    #>>main loop for calculator operations
    while True: 
        print("\n" + "="*45)
        print("        SMART CALCULATOR")
        print("="*45)
        print(" 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Modulus\n 6.history\n 7.clear history\n 8.Exit")
        #>>taking user choice and validating it
        try:
            n=int(input("Enter your choice:"))
        except ValueError:
            print("INVALID INPUT! Please enter a valid option.")
            continue
        #>>handling user choice and performing corresponding operations
        if n==8:
            print("Exiting the calculator. Goodbye!")
            break
        #calculation history
        elif n==6:
            if history_list:
                print("Calculation History:")
                for idx, res in enumerate(reversed(history_list), 1):
                    print(f"{idx}. {res}")
            else:
                print("No calculations have been made yet.")
        #clear history
        elif n==7:
            history_list.clear()  
            with open("history.txt", "w") as f: 
                f.write("")
            print("History cleared successfully.")
        #performing operations based on user choice
        elif n in [1,2,3,4,5]:
            a,b=input_number()
            match n:
                case 1:
                    result = add(a,b)
                    op="+"
                case 2:
                    result = sub(a,b)
                    op="-"
                case 3:  
                    result = mul(a,b)
                    op="*"
                case 4:
                    result = divi(a,b)
                    op="/"
                case 5:
                    result = modulus(a,b)
                    op="%"
            #>>checking if result is a valid number before printing and storing in history
            if isinstance(result, (int,float)):  
                #converting a,b into a whole number if they are integers 
                a=int(a)  if a.is_integer() else a
                b=int(b)  if b.is_integer() else b
                print(f"The result of {a} {op} {b} is: {result:.2f}")
                #getting current time and formatting it for history entry
                current_time = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")  
                final_result= f"[{current_time}] -> {a} {op} {b} = {result:.2f}"  
                history_list.append(final_result) 
                # Limit history to last 10 calculations
                if len(history_list) > 10:  
                    history_list.pop(0)  
                #sync the list & file
                with open("history.txt", "w") as f:  
                        for item in history_list:
                            f.write(item + "\n")
            else:
                print(result)
        else:
            print("INVALID INPUT! Please enter a valid option among 1-8.")
calculator()

