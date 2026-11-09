# Problem: Count the Pairs - ordered pairs (i, j), i != j, with A[i] + A[j] <= X
# Approach: sort; for each i, bisect_right(arr, X - arr[i]) = count of values <= X - arr[i];
#   subtract 1 if i itself is inside that range (i < index) so i isn't paired with itself
# Complexity: O(N log N)
# Accepted first attempt.
# Notes:
#   - bisect_right returns the first index with value > target, which is also the COUNT of values <= target
#   - `if index == 0: continue` is redundant: the ternary already adds 0
#   - ternary: ans += index if index <= i else index - 1
# (Two pointers on the sorted array also solves it in O(N) after sorting.)

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n, x = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = 0
    for i in range(0,n):
        diff = x - arr[i]
        # first value of arr[j] that is less than equal to x - arr[i]
        index = bisect_right(arr,diff)
        if index == 0:
            continue
        ans += index if index <= i else index - 1
    out.append(ans)
print("\n".join(map(str,out)))
