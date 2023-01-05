f = open("input.txt", "r")
lines = f.readlines()
f.close()

score1 = 0
score2 = 0
for line in lines:
    tmp = line.strip().split(',')
    left,right = tmp[0],tmp[1]
    l1,l2 = left.split('-')
    r1,r2 = right.split('-')
    l1,l2,r1,r2 = int(l1),int(l2),int(r1),int(r2)
    if (l1>=r1 and l2<=r2) or (r1>=l1 and r2<=l2):
        score1+=1
    if (l1>=r1 and l2<=r2) or (r1>=l1 and r2<=l2) or (r1>=l1 and r1<=l2) or (r2>=l1 and r2<=l2) or (l1>=r1 and l1<=r2) or (l2>=r1 and l2<=r2):
        score2+=1
print(score1,score2)