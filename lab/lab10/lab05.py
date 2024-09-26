def merge(list1,list2):
    result = list1
    for num in list2:
        i = 0
        while i < len(result):
            if result[i] > num:
                result.insert(i,num)
                break
            i += 1
    return result

print(merge([1,5,16,61,111], [2,4,5,6]))