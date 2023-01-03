try:
    total = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    result=  value/total *100
    print(f"total value is {result}%")
except ValueError:
    print("you need to enter a number. Run the program again ")
except ZeroDivisionError:
    print("Your total value cannot be zero.")
