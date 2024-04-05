n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end='')
    print()

for i in range(n):
    p = 1
    for j in range(i, n):
        print(p, end='')
        p += 1
    print()