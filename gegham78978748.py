import re

n = input('Enter Mobile number :')
r = re.fullmatch('[+][374][0-9]{10}', n)
if r is not None:
    print('Valid Number')
else:
    print('Not a valid number')