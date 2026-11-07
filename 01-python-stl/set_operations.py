# Problem: Set (AZ101) - add x / erase x / find x (YES/NO) / print (sorted) / empty
# Approach: built-in set (hash set); sort only at print time
# Complexity: O(1) average per add/erase/find; O(n log n) per print (printing is O(n) anyway)
# Mistakes I made:
#   - `from collections import set` -> ImportError; set is built in, no import
#   - `range(sorted(s))` -> TypeError; range needs a number. Loop directly: for x in sorted(s)
# Notes: discard() is the safe erase; int() the values so sorting is numeric ("10" < "9" as strings)

t = int(input())
for _ in range(t):
    s = set()
    q = int(input())
    for _ in range(q):
        op = input().split()
        if op[0] == "add":
            s.add(int(op[1]))
        elif op[0] == "erase":
            s.discard(int(op[1]))
        elif op[0] == "find":
            if int(op[1]) in s:
                print("YES")
            else:
                print("NO")
        elif op[0] == "print":
            for i in (sorted(s)):
                print(i,end=" ")
            print()
        elif op[0] == "empty":
            s.clear()
