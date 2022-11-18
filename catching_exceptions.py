num = input("Enter a number: ")
num2 = input("Enter the second number")

try:
    num = int(num)
    num2 = int(num2)

    total = num/num2

except ValueError:

    print("Invalid number Please try again")

except NameError:
    print("Cannot proceed with the calculation")
    total = "Unknown"


except ZeroDivisionError:
    print("Cannot divide a number by 0")
except Exception as e:
    print("Exception was caught")
    print(type(e))
