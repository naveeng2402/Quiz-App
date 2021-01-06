try:
    with open('text.txt') as f:
        x = f.readlines()
        x = [i.strip().replace('''"''', "'") for i in x]
        x = '\\n'.join(x)
except:
    with open('Tools/text.txt') as f:
        x = f.readlines()
        x = [i.strip().replace('''"''', "'") for i in x]
        x = '\\n'.join(x)
print(x)
