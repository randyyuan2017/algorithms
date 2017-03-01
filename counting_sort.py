import sys
n = int(sys.stdin.readline())
helper = [[] for i in range(100)]
count = [0]*100

for i in range(n):
    if i<(n/2):
        num,_ = sys.stdin.readline().split()
        num = int(num)
        count[num]+=1
        helper[num].append((num,"-"))
    else:
        num,s = sys.stdin.readline().split()
        num = int(num)
        count[num]+=1
        helper[num].append((num,s))
for i in range(100):
    for j in range(count[i]):
        print(helper[i][j][1], end=" ")

# https://www.hackerrank.com/challenges/countingsort4
# I was originally using dictionary for this question, thinking accessing info in dictionary must be faster than accessing list. Apparently I was wrong. I kept timing out until I switched to list.
# Accessing specific nodes of a list seems to be faster than reading a key value pair in a dictionary in this question