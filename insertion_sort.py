_ = input()

def sort_one(lis):
    num = lis[-1]
    leng = len(lis)
    i = leng-1
    while num<lis[i-1] and i>=1:
        lis[i] = lis[i-1]
        lis[i-1]=num
        i-=1
    return lis

lis = list(map(int,input().split()))
for i in range(2,len(lis)+1):
    lis = sort_one(lis[:i]) + lis[i:]
print(*lis)

# https://www.hackerrank.com/challenges/correctness-invariant?h_r=next-challenge&h_v=zen
# basic insertion sort