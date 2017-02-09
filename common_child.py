import time
import sys
def count_lcs(a,b):
    lis1 = [0 for i in range(len(b)+1)]
    lis2 = [0 for i in range(len(b)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if i%2==1:
                parent_list,children_list = lis1,lis2
            else:
                parent_list,children_list = lis2,lis1

            if a[i-1]==b[j-1]:
                children_list[j]=parent_list[j-1]+1
            else:
                children_list[j]=children_list[j-1] if children_list[j-1]>= parent_list[j] else parent_list[j]
    print(children_list[-1])

a,b=sys.stdin.readline().strip(),sys.stdin.readline().strip()
count_lcs(a,b)
# https://www.hackerrank.com/challenges/common-child
# I learned how to do a typical longest common substring/subsequence problem through this question
# I also learned that for this kind of matrix DP approach, you don't always need the full matrix. 
# My code was initially throwing segmentation faults due to insufficient memory when I implemented the full matrix. 
# Since I only need the current line and the line above for my calculation, I used 2 strings instead. This got rid of the segmentation fault memory issue for me.