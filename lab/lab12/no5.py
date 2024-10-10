import math

def power(s: set):
    s_list = list(s)
    
    power_set: list = []
    
    pow_set_size = int(math.pow(2, len(s)))

    for counter in range(pow_set_size):
        temp = []
        for j in range(len(s)):
            if counter & (1 << j):
                temp.append(s_list[j])
        power_set.append(frozenset(temp))
    return set(power_set)

s = {1, 2, 3}
print(power(s))