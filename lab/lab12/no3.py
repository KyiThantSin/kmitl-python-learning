def inverse(dict):
    inverse_dict = {}
    result = {}
    for key,value in dict.items():
        if value in inverse_dict:
            inverse_dict[value].add(key)
        else:
            inverse_dict[value] = set({key})
    
    for key, value in inverse_dict.items():
        result[key] = value
    print(result)

dict = {'a':'1', 'b':'2', 'c':'1', 'd':'3', 'e':'1', 'f':'2'}
inverse(dict)
