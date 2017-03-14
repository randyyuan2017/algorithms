def merge(arr,l,m,r):
    left_array = [arr[l+i] for i in range(m-l+1)]
    right_array = [arr[m+1+i] for i in range(r-m)]
    a=b=0
    left_array_length = len(left_array)
    right_array_length = len(right_array)

    for i in range(l,r+1):
        if a<left_array_length and b<right_array_length:
            arr[i]=left_array[a] if left_array[a]<=right_array[b] else right_array[b]
            if left_array[a]<= right_array[b]:
                a+=1
            else:
                b+=1
        elif a<left_array_length:
            arr[i]=left_array[a]
            a+=1
        elif b<right_array_length:
            arr[i]=right_array[b]
            b+=1
        print arr

def merge_sort(arr,l,r):
    if r>l:
        m = (l+(r-1))/2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)

a=[1,3,6,12,5,2,3,7,23,43,1]
merge_sort(a,0,len(a)-1)
print " ".join([str(num) for num in a])