from random import choice


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Eorror: Division by zero..."
    return a/b

def calculator():
    print("===+++ Welcome to CLI Calculator +++===")
    print("Operations: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        choice= input("\nEnter your choice (1-5): ")

        if choice=="5":
            print("Exiting... Goodbye!!")
            break

        if choice in ["1","2","3","4"]:
            try:
                if choice=="1":
                    print("<<== You have chosen the Addition Operation ==>>")
                elif choice=="2":
                    print("<<== You have chosen the Substractiion Operation ==>>")
                elif choice=="3":
                    print("<<== You have chosen the Multiplication Operation ==>>")
                elif choice=="4":
                    print("<<== You have chosen the Division Operation ==>>")


                num1= float(input("Enter First Number: "))
                num2= float(input("Enter Second Number: "))

                if choice=="1":
                    print("Result: ", add(num1,num2))
                elif choice=="2":
                    print("Result: ", subtract(num1,num2))
                elif choice=="3":
                    print("Result: ", multiply(num1, num2))
                elif choice=="4":
                    print("Result: ", divide(num1,num2))

            except ValueError:
                print("Invalid input !! Please enter numbers only...")
        else:
            print("Invalid choice !! Please select 1-5.")


if __name__ == "__main__":
    calculator()