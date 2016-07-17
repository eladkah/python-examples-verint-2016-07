'''
Implements toCamelCase and from_camel_case functions using regex
'''

import re

def to_camel_case(text):
    res = re.sub(r'_[a-z]', lambda m: m.group(0)[-1].upper(), text)
    return res

def from_camel_case(text):
    res = re.sub(r'[A-Z]', lambda m: '_' + m.group(0).lower(), text)
    return res

print to_camel_case('my_test_aaaa')
print from_camel_case('myTestAaaa')