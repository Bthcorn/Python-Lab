short = input("Enter a short string: ")
long = input("Enter a long string: ")
stop = False
for i in range(len(long)):
    if long[i:i + len(short)] == short:
        stop = True
        break
    
if stop == True:
    print(f"The {short} is a substring of {long}")
else:
    print(f"The {short} is not a substring of {long}")