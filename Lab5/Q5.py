try:
    while True: 
        char = input("Please enter a charactor: ")
        asc = ord((char))
        if asc == 9:
            print("Good bye, see you tomorrow.")
            break
        elif  48 <= asc <= 57 :
            print(char, " is a numeric charactor.")
        elif  65 <= asc <= 90:
            print(char + " is a capital letter and its small-case letter is " + char.lower())
        elif 97 < asc <= 122:
            print(char + " is small-case letter and its capital letter is " + char.upper())
        else:
            print(char + " is a speacial character")
except TypeError:
    print("Please enter a charactor!")