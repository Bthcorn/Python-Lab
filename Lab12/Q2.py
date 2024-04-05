myDict = {'s5301':'Fred', 's5302':'Harry', 's5303':'John', 's5304':'Fred', 's5305':'Harry'}

# def find_duplicates(myDict):
#     newDict = {}
#     for id in myDict:
#         if myDict[id] in myDict.values():
#             newDict[id] = myDict[id]
#             del myDict[id]
#     return newDict

def find_duplicates(myDict):
    duplicates = {}
    seen_values = {}

    for key, value in myDict.items():
        if value in seen_values:
            if value not in duplicates:
                duplicates[value] = [seen_values[value]]
            duplicates[value].append(key)
        else:
            seen_values[value] = key

    result_dict = {}
    for value, keys in duplicates.items():
        for key in keys:
            result_dict[key] = value

    return result_dict

myDict = {'s5301':'Fred', 's5302':'Harry', 's5303':'John', 's5304':'Fred', 's5305':'Harry'}
duplicates = find_duplicates(myDict)
print(duplicates)
