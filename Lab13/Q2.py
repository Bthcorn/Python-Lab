def list_reverse(list1):
    nlist = []
    if len(list1) == 0:
        return nlist
    else:
        nlist.append(list1[-1])
        return nlist + list_reverse(list1[:-1])
    
print(list_reverse([1, 2, 3]))