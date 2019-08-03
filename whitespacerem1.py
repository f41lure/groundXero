string = '''    vcruntime140.dll    gfv      fr
'''

for l in string:
    if l == ' ' or l == '\n':
        string = string.replace(l, '')
print(string)
