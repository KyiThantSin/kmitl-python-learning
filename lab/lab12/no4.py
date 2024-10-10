def is_subset(sub,sup):
    for i in sub:
        if i not in sup:
            return False
    return True  

sub = [1,2,3,4]
sup = [1,2,3]
print(is_subset(sub, sup))