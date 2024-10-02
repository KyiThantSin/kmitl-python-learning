def bubble_sort(list_data):
    for i in range(len(list_data)):
        for j in range(len(list_data) - i - 1):
            if list_data[j] > list_data[j+1]:
                    list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
    return list_data

print(bubble_sort([3,2,9,7]))