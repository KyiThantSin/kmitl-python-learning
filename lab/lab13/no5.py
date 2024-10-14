def subsetSumZero(ls, result = [], Sum = 0):
    if ls == []:
        return [x for x in [result] if sum(x) == 0 and x != []]
    else:
        return subsetSumZero(ls[1:], result + [ls[0]], Sum + ls[0]) + subsetSumZero(ls[1:], result, Sum)

def subsetSumZeroWithYesNo(ls):
    subsets = subsetSumZero(ls)
    if subsets:
        return "Yes", subsets
    else:
        return "No"

print(subsetSumZeroWithYesNo([-7, -3, -2, 5, 7]))
print("----------")
print(subsetSumZeroWithYesNo([2, -3, 5, 8 ,11, 23, -1]))
