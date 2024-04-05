number = eval(input("Enter a number: "))

if isinstance(number, float):
    type = (input("Type of number you want to display: Enter f: floating point, s: scientific format: "))
    if type == "f":
        print(float(number))
    elif type == "s":
        print(format(number, "10.2e"))
        
elif isinstance(number, int):
    type1 = str(input("Display binary(b), octal(o), hexadecimal(h), decimal(d): "))
    if type1 == "b":
        print("Binary: ", bin(number))
    elif type1 == "o":
        print("Octal: ", oct(number))
    elif type1 == "h":
        print("Hexadecimal: ", hex(number))
    elif type1 == "d":
        print("Decimal", number, "5d")
else:
    print("Plaese input real number or integer")