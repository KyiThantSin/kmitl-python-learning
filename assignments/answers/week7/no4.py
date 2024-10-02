def print_table(data):
    for arr in data:
        for j in arr:
            print(j, end="\t")
        print()

list1 = [
    ["X", "Y"],
    [0, 0],
    [10, 10],
    [200, 200]
]
list2 = [
    ["ID", "Name", "Surname"],
    ["001", "Guido", "van Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"]
]
print_table(list2)
print("")
print_table(list1)
