n = 32
p = 1
print("1", end='')
for i in range(n):
    if i % 2 == 1:
        p += 2
        print(str(p), end='')
        continue
    if i % 2 == 0:
        p += 1
        print(",", end=' ')
        print(str(p), end='')
        print(",", end=' ')
        continue