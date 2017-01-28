from copy import deepcopy
r,c,n=map(int,input().split())

full_map = []
for _ in range(r):
    full_map.append(["O" for _ in range(c)])
    
def generate_new_map(old_map):
    new_map = deepcopy(full_map)
    for i in range(r):
        for j in range(c):
            if old_map[i][j] == "O":
                for a in range(max(0,i-1),min(i+2,r)):
                    new_map[a][j]="."
                for a in range(max(0,j-1),min(j+2,c)):
                    new_map[i][a]="."
    return new_map

# initialization
initial_map = []
for _ in range(r):
    initial_map.append(list(str(input())))
time=[[] for _ in range(6)]
time[0]=time[1]=initial_map
time[2]=time[4]=full_map

# 4th frame
time[3]=deepcopy(generate_new_map(time[1]))
# 6th frame
time[5]=deepcopy(generate_new_map(time[3]))
    
# print map
if n>5 and n%2==0:
    n=2
elif n>5 and n%4==3:
    n=3
elif n>5 and n%4==1:
    n=5
for row in time[n]:
    print("".join(row))

# https://www.hackerrank.com/challenges/bomber-man?h_r=next-challenge&h_v=zen
# through this challenge I learned that for lists, a=b wouldn't make a copy of the list, it would assign the address of b to a, thus modifying a would change b too. This problem is solved by using the deepcopy library