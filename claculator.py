import math

def calculator():
    while True:
        print("\n" + "=" * 40)
        print("      PYTHON SCIENTIFIC CALCULATOR")
        print("=" * 40)

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Square Root")
        print("7. Power")
        print("8. Sine")
        print("9. Cosine")
        print("10. Tangent")
        print("11. Logarithm (Base 10)")
        print("12. Natural Log")
        print("13. Factorial")
        print("14. Exit")

        choice = input("\nEnter your choice (1-14): ")

        try:

            if choice == "1":
                a = float(input("First Number: "))
                b = float(input("Second Number: "))
                print("Result =", a + b)

            elif choice == "2":
                a = float(input("First Number: "))
                b = float(input("Second Number: "))
                print("Result =", a - b)

            elif choice == "3":
                a = float(input("First Number: "))
                b = float(input("Second Number: "))
                print("Result =", a * b)

            elif choice == "4":
                a = float(input("Dividend: "))
                b = float(input("Divisor: "))
                if b == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print("Result =", a / b)

            elif choice == "5":
                number = float(input("Enter Number: "))
                percent = float(input("Enter Percentage: "))
                print("Result =", (number * percent) / 100)

            elif choice == "6":
                number = float(input("Enter Number: "))
                if number < 0:
                    print("Error: Square root of negative number is not allowed.")
                else:
                    print("Square Root =", math.sqrt(number))

            elif choice == "7":
                base = float(input("Enter Base: "))
                exponent = float(input("Enter Exponent: "))
                print("Result =", math.pow(base, exponent))

            elif choice == "8":
                angle = float(input("Enter Angle (degrees): "))
                print("Sin =", math.sin(math.radians(angle)))

            elif choice == "9":
                angle = float(input("Enter Angle (degrees): "))
                print("Cos =", math.cos(math.radians(angle)))

            elif choice == "10":
                angle = float(input("Enter Angle (degrees): "))
                print("Tan =", math.tan(math.radians(angle)))

            elif choice == "11":
                number = float(input("Enter Number: "))
                if number <= 0:
                    print("Error: Logarithm is only defined for positive numbers.")
                else:
                    print("Log =", math.log10(number))

            elif choice == "12":
                number = float(input("Enter Number: "))
                if number <= 0:
                    print("Error: Natural Log is only defined for positive numbers.")
                else:
                    print("ln =", math.log(number))

            elif choice == "13":
                number = int(input("Enter Integer: "))
                if number < 0:
                    print("Error: Factorial is not defined for negative numbers.")
                else:
                    print("Factorial =", math.factorial(number))

            elif choice == "14":
                print("\nThank you for using the calculator.")
                break

            else:
                print("Invalid choice. Please select between 1 and 14.")

        except ValueError:
            print("Error: Please enter valid numeric values.")

        except Exception as e:
            print("Unexpected Error:", e)

calculator()