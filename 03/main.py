f = open("input.txt", "r")
dup = []
badge = []
tmp = []
for x in f:
    half = int(len(x)/2)
    lst1 = x[:half]
    lst2 = x[half:]
    tmp.append(x)
    if len(tmp) % 3 == 0:
        tmp.sort(key=len)
        for i in tmp[0]:
            if i in tmp[1] and i in tmp[2]:
                badge.append(i)
                break
        tmp = []
    for i in lst1:
        if i in lst2:
            dup.append(i)
            break
print(sum([ord(i)-ord('A')+27 if ord(i) < 97 else ord(i)-ord('a')+1 for i in dup]))
print(sum([ord(i)-ord('A')+27 if ord(i) < 97 else ord(i)-ord('a')+1 for i in badge]))
