f = open("input.txt", "r")
lines = f.readlines()
f.close()

scheme = []
tab1 = []
tab2 = []
for line in lines:
    if line == '\n':
        break
    else:
        scheme.append(line.replace('\n', ''))

scheme = scheme[:-1:][::-1]
[(tab1.append([]), tab2.append([])) for i in range((len(scheme[0])//4)+1)]
for row in scheme:
    str = [row[j:j+4] for j in range(0, len(row), 4)]
    for i in range(len(str)):
        if '[' in str[i]:
            tab1[i].append(str[i].strip())
            tab2[i].append(str[i].strip())
switch = False
for line in lines:
    if line == '\n':
        switch = True
        continue
    if switch:
        str = line.strip().split()
        nb, source, dest = int(str[1]), int(str[3])-1, int(str[5])-1
        length = len(tab2[dest])
        for i in range(nb):
            tab1[dest].append(tab1[source].pop())
            tab2[dest].insert(length, tab2[source].pop())

[print(i[-1].replace(']', '').replace('[', ''), end='') for i in tab1]
print()
[print(i[-1].replace(']', '').replace('[', ''), end='') for i in tab2]
