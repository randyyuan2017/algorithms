from math import floor
_,k=map(int,input().split())
num = list(map(int,input()))
leng = len(num)
half_length = floor(leng/2)
count = sum([1 if num[i]!=num[leng-i-1] else 0 for i in range(leng)])
if count>2*k:
    for i in range(half_length):
        if num[i]!=num[leng-i-1]:
            k-=1
            num[i]=num[leng-i-1]=max(num[i],num[leng-i-1])
            if k<0:
                print(-1)
                break
    if(k>=0):
        print("".join(map(str,num)))
else:
    i=half_length
    while count>k or (count<k and i>=int(k/2)):
        if num[i]!=num[leng-i-1]:
            num[i]=num[leng-i-1]=max(num[i],num[leng-i-1])
            k-=1
            count-=2
        i-=1
    i=0
    while (k>=2 and i<=half_length):
        if num[i]!=9 and num[leng-i-1]!=9:
            num[i]=num[leng-i-1]=9
            k-=2
        elif num[i]!=9 or num[leng-i-1]!=9:
            num[i]=num[leng-i-1]=9
            k-=1
        i+=1
    if k>=1 and num[half_length]!=9:
        num[half_length]=9
    print("".join(map(str,num)))

    # imcomplete!