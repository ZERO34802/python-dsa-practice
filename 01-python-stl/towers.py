# Problem: Towers (AZ101 / CSES) - place blocks in order; a block goes on a tower whose top is strictly
#   bigger; minimize the number of towers
# Approach: keep a list of tower tops (sorted). For block x, bisect_right gives the smallest top > x
#   (C++ upper_bound). Replace that top with x, or append if none exists. Answer = len(list).
# Why a plain list works (no sorted set needed): replacing tops[i] with x keeps the list sorted,
#   since tops[i-1] <= x < tops[i]; appending happens only when x >= every top.
#   Same trick as O(n log n) LIS.
# Complexity: O(N log N)
# Accepted first attempt.
# Notes:
#   - a heap can't do this: it only gives the min, and its list is in heap order, not sorted
#   - sets have no indexing; lists do
#   - `id` shadows the built-in id(); avoid naming variables id, list, max, sum, input, str
#   - bisect_left import is unused

from bisect import bisect_right,bisect_left

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    finalarr = []
    for i in range(0,n):
        id = bisect_right(finalarr, arr[i])
        if id != len(finalarr):
            finalarr[id] = arr[i]
        else:
            finalarr.append(arr[i])
    print(len(finalarr))
