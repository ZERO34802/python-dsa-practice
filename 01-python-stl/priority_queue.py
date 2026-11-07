# Problem: Priority Queue - add x / remove top (if non-empty) / print top (0 if empty)
# Approach: heapq is a MIN-heap -> push -x to get a max-heap, negate again when reading
# Complexity: O(log n) per add/remove, O(1) per print
# Mistakes I made:
#   - checked op[1] in the one-word branch -> IndexError; the word is op[0]
#   - heapq.heappop() without the list -> TypeError; heapq functions take the list: heappop(pq)
#   - no empty checks -> pq[0] / heappop crash on an empty heap; guard with `if pq:`
# Style: -n instead of -1*n

import heapq

t = int(input())
for _ in range(0,t):
    pq = []
    q = int(input())
    for _ in range(q):
        op = input().split()
        if len(op) > 1:
            n = int(op[1])
            heapq.heappush(pq,-1*n)
        else:
            if op[0] == "print":
                if len(pq) > 0:
                    print(-1*pq[0])
                else:
                    print(0)
            else:
                if len(pq) > 0:
                    heapq.heappop(pq)
