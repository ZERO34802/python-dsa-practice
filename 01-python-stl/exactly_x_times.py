# Problem: Remove the fewest elements so every value x appears exactly x times
# Approach: count frequencies; for each value, remove v - k extras if v > k, else remove all v
# Complexity: O(n)
# Mistakes I made:
#   - plain dict mp[x] += 1 on a missing key -> KeyError; use defaultdict(int)
#   - read the array one number per line, but it was on one line -> list(map(int, input().split()))
#   - `from Collections` -> module names are lowercase: `from collections`
#   - first logic added all v whenever k != v; the v > k case only needs v - k removals
# Idiom: `for x in arr: mp[x] += 1`, or Counter(arr) for the whole loop

from collections import defaultdict
t = int(input())
for _ in range(1, t + 1):
    n = int(input())
    arr = []
    mp = defaultdict(int)
    arr = list(map(int,input().split()))
    for i in range(0,n):
        mp[arr[i]] += 1
    ans = 0
    for k,v in mp.items():
        if k != v:
            if v > k:
                ans += (v - k)
            else:
                ans += v
    print(ans)
