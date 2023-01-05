f = open("input.txt","r")
"""
  R P S
R 0 1 2
P 2 0 1
S 1 2 0

"""
score1,score2 = 0,0
rps = [[3,6,0],[0,3,6],[6,0,3]]
for x in f:
    tmp = x.split()
    if tmp[1] == 'X':
        pick = rps[ord(tmp[0])-ord('A')].index(0)
    elif tmp[1] == 'Y':
        pick = rps[ord(tmp[0])-ord('A')].index(3)
    else:
        pick = rps[ord(tmp[0])-ord('A')].index(6)
    score2 += rps[ord(tmp[0])-ord('A')][pick]+pick+1
    score1+= rps[ord(tmp[0])-ord('A')][ord(tmp[1])-ord('X')]+ ord(tmp[1])-ord('X')+1
print(score1,score2)

