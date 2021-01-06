import sys
func = sys.argv[1]

with open('text.txt') as f:
    x = f.readlines()
    x = [i.strip() for i in x]


for i in x:
    print(f'''{func}(f\'\'\'{i}\'\'\')''')
