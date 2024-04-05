sup = set([1, 2, 3, 4])
sub = set()

def is_subset(sub, sup):
    now = True
    for x in sub:
        if not x in sup:
            now = False
    return now

print(is_subset(sub, sup))

sub = set([1, 2, 4, 5])
print(is_subset(sub, sup))
