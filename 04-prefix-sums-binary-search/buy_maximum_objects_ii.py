# Problem: Buy Maximum Objects II - N prices; Q queries with money M: max number of objects you can buy
# Approach: greedy - buy cheapest first. Sort, prefix sums, answer = bisect_right(pref, M)
#   (= number of prefix sums <= M, i.e. C++ upper_bound - begin)
# Complexity: O(N log N + Q log N)
# Mistakes I made:
#   - set pref[0] = arr[0] BEFORE arr.sort() -> pref[0] used the unsorted first price (WA)
# Simplification: bisect_right already returns n when everything fits, so the if/else can be
#   out.append(bisect_right(pref, m))

import sys
from bisect import bisect_right,bisect_left
input = sys.stdin.readline

n, q = map(int,input().split())
arr = list(map(int,input().split()))
pref = [0]*n
arr.sort()
pref[0] = arr[0]
for i in range(1,n):
    pref[i] = pref[i - 1] + arr[i]
out = []
for _ in range(q):
    m = int(input())
    index = bisect_right(pref,m)
    if index == len(pref):
        out.append(n)
    else:
        out.append(index)
print("\n".join(map(str,out)))
