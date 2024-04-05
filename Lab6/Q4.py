sum = 0
def sum_of_digits(x):
    global sum
    list = []
    for i in str(x):
        list.append(int(i))

    for j in list:
        sum += j
    return sum

print(sum_of_digits(123456789))

