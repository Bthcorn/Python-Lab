num = int(input("Enter the number of lines: "))

# num = 5

for i in range(0, num // 2):
    for j in range(i, -1, -1):
        print(2**j, end=' ')
    print()

if num % 2 == 0:
    for i in range(num // 2, 0, -1):
        for j in range(i, 0, -1):
            print(2**(j-1), end=' ')
        print()
else: 
    for i in range(num // 2 + 1, 0, -1):
        for j in range(i, 0, -1):
            print(2**(j-1), end=' ')
        print()
# if num % 2 == 1:
#     for i in range(1, num):
#         for j in range(1, i+1):
#             print(p*2, end=' ')
#             p += 1
#         print()