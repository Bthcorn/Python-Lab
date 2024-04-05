def grade(score):
    if 80 <= score <= 100:
        return "A"
    elif 70 <= score < 80:
        return "B"
    elif 60 <= score < 70:
        return "C"
    elif 50 <= score < 60:
        return "D"
    elif 0 <=score < 50:
        return "F"
    else:
        return "Invalid score"
    
def main():
    print("His/her grade is", grade(68))

main()