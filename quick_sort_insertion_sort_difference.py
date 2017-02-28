leng = int(input())-1
quick_sort_lis = list(map(int,input().split()))
insertionsort_lis = list(quick_sort_lis)
quicksort_count = 0
insertionsort_count = 0

def sort_lis(first,last):
	global quick_sort_lis
	global quicksort_count
	if last>first:
		pivot, ltp = quick_sort_lis[last],first
		for i in range(first,last):
			if quick_sort_lis[i]<pivot:
				quick_sort_lis[i],quick_sort_lis[ltp]=quick_sort_lis[ltp],quick_sort_lis[i]
				quicksort_count+=1
				ltp+=1
		quick_sort_lis[last],quick_sort_lis[ltp]=quick_sort_lis[ltp],quick_sort_lis[last]
		quicksort_count+=1
		sort_lis(first,ltp-1)
		sort_lis(ltp+1,last)

def sort_one(lis):
    global insertionsort_count
    num = lis[-1]
    leng = len(lis)
    i = leng-1
    while num<lis[i-1] and i>=1:
        lis[i] = lis[i-1]
        lis[i-1]=num
        i-=1
        insertionsort_count+=1
    return lis

for i in range(2,len(insertionsort_lis)+1):
    insertionsort_lis = sort_one(insertionsort_lis[:i]) + insertionsort_lis[i:]
sort_lis(0,leng)
print(insertionsort_count-quicksort_count)

# https://www.hackerrank.com/challenges/quicksort4