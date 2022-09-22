from encodings import utf_8
from traceback import print_list
with open('task4.txt', 'r', encoding = 'utf_8') as f:
    for line in f.readlines():
        print(line)
count = 1
line = line + ' '
line_new = ''
for i in range(len(line)-1):
    if line[i] == line[i + 1]:
        count += 1
    else:
        line_new = line_new + (str(count) + line[i])
        count = 1
print(line_new)
f = open('task4.txt','a', encoding = 'utf_8')
f.write(('\n' + line_new))
f.close()