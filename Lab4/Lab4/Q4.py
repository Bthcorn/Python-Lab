char = input("Please enter a charactor: ")

asc = ord((char))

if  48 <=asc <= 57 :
    print(char, " is a numeric charactor.")
elif 65 <=asc <= 97:
    print(char + " is a capital letter and its small-case letter is " + char.lower())
elif 97 <=asc <= 123:
    print(char + " is small-case letter and its capital letter is " + char.upper())
else:
    print(char)