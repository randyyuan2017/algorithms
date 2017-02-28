leng = int(input())-1
lis = list(map(int,input().split()))

def sort_lis(first,last):
	global lis
	if last>first:
		pivot, ltp = lis[last],first
		for i in range(first,last):
			if lis[i]<pivot:
				lis[i],lis[ltp]=lis[ltp],lis[i]
				ltp+=1
		lis[last],lis[ltp]=lis[ltp],lis[last]
		print(*lis)
		sort_lis(first,ltp-1)
		sort_lis(ltp+1,last)

sort_lis(0,leng)

# https://www.hackerrank.com/challenges/quicksort3
# sorting is still very very rusty :(
# I learned the Lomuto Partitioning technique for doing in place quicksorts through this question