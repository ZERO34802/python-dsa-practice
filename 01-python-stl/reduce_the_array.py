# Problem: Reduce the Array (AZ101) - repeatedly merge two elements (cost = their sum) until one remains; minimize cost
# Approach: Huffman / optimal-merge greedy with a min-heap: pop two smallest, add sum to cost, push sum back
# Complexity: O(N) heapify + O(N log N) merges
# Mistakes I made:
#   - input().list() -> AttributeError; strings have .split(), and list(map(...)) already makes the list
# Notes: heapq is a min-heap already (no negation); `while len(pq) > 1` handles N = 1 (cost 0)

import heapq
t = int(input())
for _ in range(0,t):
    n = int(input())
    pq = list(map(int,input().split()))
    heapq.heapify(pq)
    cost = 0
    while len(pq) > 1:
        t1 = heapq.heappop(pq)
        t2 = heapq.heappop(pq)
        cost += (t1 + t2)
        heapq.heappush(pq,t1 + t2)
    print(cost)
