def count_difference(lis, sorted_lis):
    count=0
    lis_map = {lis[i]:i for i in range(len(lis))}
    for i in range(len(lis)):
        if lis[i]!=sorted_lis[i]:
            correct_val_index = lis_map[sorted_lis[i]]
            lis[i],lis[correct_val_index]=lis[correct_val_index],lis[i]
            lis_map[lis[correct_val_index]]=correct_val_index
            count+=1
    return count

lis = [2,5,3,1]
lis_a=list(lis)
lis_b=list(lis)
sorted_lis = sorted(lis)
reversed_sorted_lis = sorted_lis[::-1]
print(min(count_difference(lis_a, sorted_lis),count_difference(lis_b,reversed_sorted_lis)))

# https://www.hackerrank.com/challenges/lilys-homework
# the algorithm used for this question is from the discussion of the question