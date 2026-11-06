# Problem: Print all permutations of 1..n in lexicographic order, one per line
# Approach: itertools.permutations on an already-sorted input yields lexicographic order
# Complexity: O(n * n!)
# Mistakes I made:
#   - print(ans) printed the whole list on one line -> loop and print each permutation
#   - nested loop over `ans` twice printed everything n! times -> inner loop must be over `p`
#   - forgot print() after print(x, end=" ") -> everything landed on one line
# Note: permutations yields TUPLES and follows input positions (sort first; duplicates repeat)

from itertools import permutations

n = int(input())
arr = [0]*n
for i in range(0,n):
    arr[i] = i + 1
ans = []
for p in permutations(arr):
    ans.append(p)
ans.sort()
for p in ans:
    for x in p:
        print(x, end=" ")
    print()
