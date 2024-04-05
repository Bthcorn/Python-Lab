A = int(input("Enter an integer"))

if A % 2 == 0:
    for x in range(1, (A - (A // 2)) + 1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

    for x in range((A - (A // 2)), 0, -1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

if A % 2 != 0:
    for x in range(1,(A - ((A+1) // 2)) + 1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

    for x in range((A - ((A-1) // 2)), 0, -1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()
# n = 5

# # Upper half of the pattern
# for i in range(1, n+1):
#     num = i
#     for j in range(i):
#         print(num, end=" ")
#         num -= 1
#     print()

# # Lower half of the pattern
# for i in range(n-1, 0, -1):
#     num = i
#     for j in range(i):
#         print(num, end=" ")
#         num -= 1
#     print()