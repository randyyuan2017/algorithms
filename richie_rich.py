from math import ceil
_,k=map(int,input().split())
num = list(map(int,input()))
leng = len(num)
half_length = ceil(leng/2)-1
count = sum([1 if num[i]!=num[leng-i-1] else 0 for i in range(leng)])
if count>2*k:
    print(-1)
else:
    i=half_length
    new_count = (leng - num.count(9))
    while new_count>k:
        if i == half_length and leng%2==1:
            new_count -= 1 - [num[i]].count(9)
        else:
            new_count -= (2-[num[i],num[leng-i-1]].count(9))
        if num[i]!=num[leng-i-1]:
            num[i]=num[leng-i-1]=max(num[i],num[leng-i-1])
            k-=1
        i-=1
    i=0
    while ((k>1 or (k>0 and (num[i]==9 or num[leng-i-1]==9))) and i<=half_length):
        if num[i]!=9 and num[leng-i-1]!=9:
            num[i]=num[leng-i-1]=9
            k-=2
            new_count-=2
        elif num[i]!=9 or num[leng-i-1]!=9:
            num[i]=num[leng-i-1]=9
            k-=1
            new_count-=1
        i+=1
    if k>=1 and num[half_length]!=9:
        num[half_length]=9
    print("".join(map(str,num)))

# https://www.hackerrank.com/challenges/richie-rich
# complete version.  
# 3 places I struggled the most were:  
# 1: when replacing numbers with 9s to maximize, I didn't count the 9s at the end of the number  
# 2: when counting the number of replacements needed(new_count), I didn't count the 9s that are naturally in the number
# 3: when splitting the number in half, I did floor(leng/2) at first, this is one number too big for even numbers. ceil(leng/2)-1 gives the last index of the first half of any number.