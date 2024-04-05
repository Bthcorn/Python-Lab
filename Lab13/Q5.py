def subset_sum(list1, index=0, current= None, result= None):
    if current is None:
        current = []
    if result is None:
        result = []
    if index == len(list1):
        if sum(current) == 0 and len(current) != 0:
            result.append(current.copy())
        return
    current.append(list1[index])
    subset_sum(list1, index + 1, current, result)
    current.pop()
    subset_sum(list1, index + 1, current, result)
    if index == 0:
        if len(result) <= 1:
            return "No"
        else:
            return f"Yes {result}"
        
list1 = [-7, -3, -2, 5, 7]
list2 = [2, -3, 5, 8, 11, 23, -1]


def subsetSum(l: list = [], note = None):
    if note == None:
        note = []
    if l == []:
        if sum(note) == 0 and note != []:
            return [tuple(note)]
        return []
    return subsetSum(l[1:], note) + subsetSum(l[1:], note + [l[0]])
print(subsetSum(list1))
print(subsetSum(list2))

def sum_sub(wait, current=[]):
    if len(wait) == 0:
        if sum(current) == 0:
            return [current]
        return []
        
    new_wait = wait[1:]
    new_current = current + [wait[0]]
    include = sum_sub(wait=new_wait, current=new_current)
    exclude = sum_sub(wait=new_wait, current=current)
    return include + exclude

print(sum_sub(list1))
print(sum_sub(list2))
