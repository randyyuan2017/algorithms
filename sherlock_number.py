from collections import Counter
s_count=Counter(input())
s_min_key = min(s_count, key=s_count.get)
s_min = s_count[s_min_key]
if s_min == 1:
    del s_count[s_min_key]
    if s_count==Counter():
        print("Yes")
    else:
        new_s_min= s_count[min(s_count, key=s_count.get)]
        print("YES" if sum([s_count[k]-new_s_min for k in s_count])==0 else "NO")
else:
    print("YES" if sum([s_count[k]-s_min for k in s_count])<=1 else "NO")


# https://www.hackerrank.com/challenges/sherlock-and-valid-string
# This question is pretty easy. I'm only putting it here because it's worth a ridiculous amount of points on HR.