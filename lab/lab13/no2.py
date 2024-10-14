def list_reverse(data):
    if len(data) == 0:
        return []
    else:
        return list_reverse(data[1:]) + [data[0]]
#     print(result_list)

print(list_reverse([1,2,3]))
