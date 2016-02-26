s = '-4.5+6y=7x+8'
l = s.replace('-', '+-').split('=')
d = l[0].split('+')
for i in l[1].split('+'):
    if i.startswith('-'):
        d.append(i[1:])
    else:
        d.append('-' + i)
dict_ = {'x':0, 'y':0, 'const':0}
for item in d:
    if item == '':
        continue
    if item[-1] == 'x':
        dict_['x'] += eval(item[:-1])
    elif item[-1] == 'y':
        dict_['y'] += eval(item[:-1])
    else:
        dict_['const'] += eval(item)

print(dict_)


'''
def get_function_string():
    import re
    re_variable = re.compile(r'[a-zA-z]+')
    while True:
        function_string = input('Please input equation:')
        if not EQUAL_SIGN in function_string:
            print('ERROR')
            break
        variable = list(set(re_variable.findall(function_string))) + ['constant']
        if len(variable) < 2:
            print('ERROR')
            break
        list_for_two_sides = function_string.replace('-', '+-').split('=')
'''
