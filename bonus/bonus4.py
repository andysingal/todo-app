try:
    width = float(input("Enter rectangular width: "))
    length = float(input("Enter rectangular length: "))
    if width == length:
        exit("This is a square")
    else:
        area = width * length
        print(area)
except  ValueError:
    print("Enter a number")
