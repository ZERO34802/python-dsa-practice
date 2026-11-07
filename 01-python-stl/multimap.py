# Problem: Multimap (AZ101) - add name marks / erase first entry / eraseall / print first entry (0 if none)
# Approach: defaultdict(deque): append to add, popleft to erase the first entry (O(1)), del to erase all
# Complexity: O(1) per query
# Mistakes I made (several rounds):
#   - add used s[0] (the word "add") as the name; parts are ["add", name, marks]
#   - print read mp[x], a stale variable from the last add; use the query's own name s[1]
#   - print condition was inverted (printed 0 when the name existed)
#   - called popleft() on a list -> AttributeError; popleft is a deque method (list has pop(0), O(n))
#   - `import deque` -> deque lives in collections: from collections import defaultdict, deque
#   - del / popleft / [0] on missing or EMPTY entries crash; a key can exist with an empty deque
#     after erases, so `in mp` alone is not enough -> also check it is non-empty
# Idiom: `if mp[s[1]]:` is the short non-empty check (an empty deque counts as false)

from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    mp = defaultdict(deque)
    q = int(input())
    for _ in range(q):
        s = input().split()
        if s[0] == "add":
            x = s[1]
            y = s[2]
            mp[x].append(y)
        elif s[0] == "erase":
            if s[1] in mp and len(mp[s[1]]) > 0:
                mp[s[1]].popleft()
        elif s[0] == "eraseall":
            if s[1] in mp:
                del mp[s[1]]
        else:
            if s[1] in mp and len(mp[s[1]]) > 0:
                print(mp[s[1]][0])
            else:
                print(0)
