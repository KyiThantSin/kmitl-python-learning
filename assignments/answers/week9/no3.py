set1 = set([1, 2, 3])
set2 = set(['p', 'q'])
set3 = set(['a', 'b', 'c'])

def product(*sets):
    if not sets:
        return [()]
    result = [[]]
    for s in sets:
        result = [x + [y] for x in result for y in s]
    return set([tuple(item) for item in result])

result1 = product(set1)
print(result1)

result2 = product(set1, set2)
print(result2)

result3 = product(set1, set2, set3)
print(result3)