try :
    score = int(input("Enter a score: "))
    if score < 0 or score > 100:
        print("You need to input number in range from 0 to 100.")
    elif 80 <= score and score <=100 :
        print("Your grade: Grade A")
    elif 70 <= score and score < 80:
        print("Your grade: B")
    elif 60 <= score and score < 70:
        print("Your grade: C")
    elif 50 <= score and score < 60:
        print("Your grade: D")
    elif score < 50:
        print("Your grade: F")
except ValueError:
    print("You need to input number in range from 0 to 100.")