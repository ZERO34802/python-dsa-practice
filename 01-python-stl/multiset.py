# Problem: Multiset (AZ101) - add / erase one / eraseall / find / count / print (sorted, with duplicates) / empty
# Approach: count map (defaultdict(int)) + set of present values; sort distinct values only at print time
# Complexity: O(1) average per update; print is O(d log d + total printed), d = distinct values
# Mistakes I made:
#   - first = op[1] -> IndexError on one-word queries; the operation is op[0]
#   - print looped over the set once per value -> lost duplicates; print x mp[x] times
#   - empty cleared st but not mp -> count after empty returned stale counts (WA)
# Simplification: mp alone is enough if keys are deleted at 0 (x in mp = present; sorted(mp) = values),
#   so there is only one container to keep in sync
# Cost note: C++ multiset pays O(log n) per insert to stay sorted; this pays at print time instead

from collections import defaultdict
t = int(input())
for _ in range(t):
    q = int(input())
    mp = defaultdict(int)
    st = set()
    for _ in range(q):
        op = input().split()
        first = op[0]
        if first == "add":
            second = int(op[1])
            if second in st:
                mp[second] += 1
            else:
                st.add(second)
                mp[second] = 1
        elif first == "count":
            second = int(op[1])
            print(mp[second])
        elif first == "erase":
            second = int(op[1])
            if second in st:
                mp[second] -= 1
                if mp[second] == 0:
                    st.discard(second)
        elif first == "eraseall":
            second = int(op[1])
            if second in st:
                mp[second ] = 0
                st.discard(second)
        elif first == "find":
            second = int(op[1])
            if second in st:
                print("YES")
            else :
                print("NO")
        elif first == "empty":
            st.clear()
            mp.clear()
        elif first == "print":
            for x in sorted(st):
                for _ in range(0,mp[x]):
                    print(x,end=" ")
            print()
