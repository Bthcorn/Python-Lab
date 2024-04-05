dict = {'a':'1', 'b':'2', 'c':'1', 'd':'3', 'e':'1', 'f':'2'}

def inverse(dict):
    newDict = {}
    for key in dict.keys():
        if dict[key] in newDict.keys():
            newDict[dict[key]].add(key)
        else:
            newDict[dict[key]] = set([key])
    return newDict

inverted_dict = inverse(dict)
print(inverted_dict)
