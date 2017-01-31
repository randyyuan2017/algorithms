from functools import reduce
for _ in range(int(input())):
    _, lis = input(), list(map(int,input().split()))
    if set(lis)=={1}:
        print("First" if len(lis)%2==0 else "Second")
    else:
        print("Second" if reduce(lambda a,b:a^b, lis)==0 else "First")

# https://www.hackerrank.com/challenges/misere-nim-1
# this question is similar to the nims question, but it has an extra twist

# for original nim: since the winning move turns a list whose XOR value is not 0 to 0, any move that turns the list's XOR value from 0 to not 0 is not a winning move.
# when the list's XOR value is 0, any move makes its XOR value not 0
# when the list's XOR value is not 0, there's always a move that can make its XOR value 0
# hence, the player with the winning hand can always keep his winning hand by turning the list's XOR value to 0, forcing his opponent to turn the list's XOR value to non 0 again

# This question is slightly different in that when all piles only has 1 stone, the XOR value actually reflects the opposite of who's winning