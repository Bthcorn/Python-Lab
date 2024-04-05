def LCS(s1, s2):
    max_len = 0
    string = ""
    for i in range(len(s1)):
        for j in range(i, len(s1) + 1):
            common = s1[i:j]
            if common in s2:
                if len(common) > max_len:
                    max_len = len(string)
                    string = common
    return string
print(LCS("ingenious", "intelligent"))
print(LCS("ingenious", "inconsidered"))
print(LCS("russian", "ukranian"))
print(LCS("war", "love"))
print(LCS("romanian", "roman"))
