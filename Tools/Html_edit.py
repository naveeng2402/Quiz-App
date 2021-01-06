with open('text.txt') as f:
    x = f.readlines()
    x = [i.strip() for i in x]
    x = '\\n'.join(x)

print(x)