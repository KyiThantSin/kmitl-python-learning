def check_substring(x, y):
    if len(x) > len(y):
        return False

    for i in range(len(y) - len(x)):
        temp = ""
        for j in range(len(x)):
            temp += y[j + i]
        if temp == x:
            return f"'{x}' is a substring of {y}."

    return f"'{x}' is not a substring of {y}."

print(check_substring("hi","hekko"))