# Problem: Maximum in Window - max of every window of size K
# Approach: "multiset" stand-in = max-heap with LAZY DELETION.
#   Push (-A[i], i). Never erase when an element leaves the window; when reading the max,
#   pop tops whose index < i - K + 1 (dead) until the top is inside the window.
#   (Classic alternative: monotonic deque, O(N).)
# Complexity: O(N log N) - each element pushed once, popped at most once
# Why not a sorted list + bisect: insort / pop(i) shift O(K) elements -> O(N*K) worst case, TLE for big K
# Mistakes I made:
#   - output separator ".\n" (typo) then "\n" -> the format is one line per test case: " ".join(...)
#     (the string before .join is what goes BETWEEN elements; print adds the final newline)
# Tuples: (a, b) is a pair; p[0] / p[1] or unpack `f, s = p`; heap top's fields are pq[0][0], pq[0][1]

import heapq, sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    out = []
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    pq = []
    for i in range(0,n):
        heapq.heappush(pq,(-1*arr[i],i))
        if i >= (k - 1):
            while len(pq) > 0:
                f,s = pq[0]
                if s >= (i - k + 1):
                    out.append(-1*f)
                    break
                heapq.heappop(pq)
    print(" ".join(map(str,out)))
