'''
returns dictionary where key is result of function and value is list of strings that returned the same result
'''

def group_by(s, *words):
    dictionary = {}
    for word in words:
        key = s(word)
        if key in dictionary:
            dictionary[s(word)].append(word)
        else:
            dictionary[s(word)] = [word]

    return dictionary

print group_by(lambda(s): s[0], 'hello', 'hi', 'help', 'bye', 'here')
