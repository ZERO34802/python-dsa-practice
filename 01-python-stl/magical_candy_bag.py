# Problem: The Magical Candy Bag (AZ101) - K minutes; each minute eat the largest bag, it becomes floor(A/2)
# Approach: greedy with a max-heap (heapq + negation); pop max, add to answer, push back max // 2
# Complexity: O(N log N + K log N)
# Accepted first attempt.
# Trap avoided: halve the POSITIVE value, then negate. -7 // 2 == -4 (Python floors), so halving
#   the negated value directly would be wrong.
# Idioms for next time:
#   - top = -heapq.heappop(pq)  (heappop returns the value)
#   - pq = [-x for x in arr]; heapq.heapify(pq)  -> O(n) build instead of n pushes

import heapq
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    pq = []
    arr = list(map(int,input().split()))
    for i in range(0,n):
        heapq.heappush(pq,-1*arr[i])
    ans = 0
    for _ in range(k):
        top = -1*pq[0]
        heapq.heappop(pq)
        ans += top
        heapq.heappush(pq,-1*(top//2))
    print(ans)
