result = 0
for item in range(5):
    number = int(input("Entrt an integer: "))
    if (result >= 0 and number >=0) or (result < 0 and number < 0):
        result += number
        print("Current sum:", result)
    else :
        result = number
        print("Current sum:", result)