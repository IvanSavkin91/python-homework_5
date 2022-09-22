with open("task1.txt", "r+", encoding = 'utf_8') as f:
    for line in f.readlines():
        print(line)
line = list(filter(lambda x: 'ццц' not in x, line.split()))
line = ' '.join(line)
print(line)


f = open('task1.txt','a', encoding = 'utf_8')
f.write('\n' + line)
f.close()