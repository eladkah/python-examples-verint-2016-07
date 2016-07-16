'''
my_method receives a number and string as parameters and validates them.
'''

def my_method(num, string):
    if type(num) != int:
        raise Exception("num parameter must be a number")
    if type(string) != str:
        raise Exception("string parameter must be a string")

my_method(1, 'a')
