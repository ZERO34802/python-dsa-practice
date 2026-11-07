# Problem: Common Absolute Difference (maang.in #379) - count pairs i < j with |A[i] - A[j]| = K
# Approach: walk left to right; for each A[j], add counts of earlier A[j] - K and A[j] + K from a defaultdict
# Complexity: O(N) average per test case
# Mistakes I made:
#   - first tried prefix sums (that's the subarray-sum = K pattern, LC 560), not pairs of elements
#   - `return ans` at top level -> SyntaxError; top-level code prints, return only works inside def
# Judge note: 9/12 tests passed; the failing tests are locked. If K = 0 ever appears,
#   A[j] - K and A[j] + K are the same key and get counted twice -> guard with `k != 0 and ...`

from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = 0
    mp = defaultdict(int)
    for i in range(0,n):
        if (arr[i] - k) in mp:
            ans += mp[arr[i] - k]
        if (arr[i] + k) in mp:
            ans += mp[arr[i] + k]
        mp[arr[i]] += 1
    print(ans)
