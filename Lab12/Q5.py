s = set([1, 2, 3])

# s = set([1, 2, 3])
def power_set(s):
    lst = list(s)
    n = len(lst)
    powerset = set()

    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(lst[j])
        powerset.add(frozenset(subset))

    return powerset

print(power_set(s))

