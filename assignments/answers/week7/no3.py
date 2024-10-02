def my_union(list1, list2):
    data = [item for item in list2 if item not in list1]
    list1.extend(data)
    return list1

def my_intersection(list1, list2):
    data = [item for item in list1 if item in list2]
    return data

def my_difference(list1, list2):
    result_item1 = [item for item in list1 if item not in list2]
    result_item1
    return result_item1

print("Union:",my_union([3,1,2,7],[4,1,2,5]))
print("Intersection:", my_intersection([3,1,2,7],[4,1,2,5]))
print("Difference:", my_difference([3,1,2,7],[4,1,2,5]))
