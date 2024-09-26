def get_the_difference(list1, list2):
    result_item2 = [item for item in list2 if item not in list1]
    result_item1 = [item for item in list1 if item not in list2]
    result_item1.extend(result_item2)
    return result_item1

print(get_the_difference([3,1,1,1,2,7],[4,1,1,2,2,5]))

