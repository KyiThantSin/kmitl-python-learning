def remove_the_thirds(input_list):
    result_result = []
    for i in range(len(input_list)):
        if(i + 1) % 3 != 0:
            result_result.append(input_list[i])
    input_list = result_result
    return input_list
    
list2 = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]
print(remove_the_thirds(list2))
