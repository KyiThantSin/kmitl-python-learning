dict1 = {
    'a': 'p',
    'b': 'r',
    'c': 'q',
    'd': 'p',
    'e': 's'
}

dict2 = {
    'p': '1',
    'q': '2',
    'r': '3'
}

def composite(dict1, dict2):
    dict3 = {}
    for k, m1 in dict1.items():
        for m2, v in dict2.items():
            if m1 == m2 and k not in dict3:
                dict3[k] = v
            else:
                pass
    return dict3

print(composite(dict1, dict2))