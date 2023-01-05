f = open("input.txt","r")
i = 0
l = [0]
for x in f:
    if x =='\n':
        i+=1
        l.append(0)
        continue
    l[i]+=int(x)
mx = max(l)
print('Part1 :',mx)

l.sort(reverse=True)
print('Part2 :',sum(l[0:3]))