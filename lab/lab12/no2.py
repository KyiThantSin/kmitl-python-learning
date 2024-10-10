def find_duplicates(dict):
    reverse_dict = {}
    result = {}
    for key, value in dict.items():
        if value not in reverse_dict:
            reverse_dict[value] = [key]  
        else:
            reverse_dict[value].append(key)  
    
    for value, keys in reverse_dict.items():
        if len(keys) > 1:
            result[value] = reverse_dict[value]
    print(result)

find_duplicates({'s5300': 'Fred', 's5302': 'Harry', 's503': 'Fred', 's506': 'John', 's508': 'Harry'})
