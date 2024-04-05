def list_member(n, list1):
    if len(list1) == 0:
        return False
    if n == list1[0]:
        return True
    else:
        return list_member(n, list1[1:])

print(list_member(2, [1,2,3]))