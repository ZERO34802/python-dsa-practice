# Problem: Students and Grades - for each section-B student (in entry order), is someone already
#   in the room (section A or earlier B students) with the same marks?
# Approach: hash set of marks in the room; check, then add each B student as they enter
# Complexity: O(N + M) average
# Accepted first attempt. Key detail: add B students to the set after checking them.
# Idioms for next time:
#   - seta = set(arr)  builds the set in one line
#   - print("YES" if i in seta else "NO")
# Note: marks up to 1e12 -> long long in C++; Python ints never overflow

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    seta = set()
    arr = list(map(int,input().split()))
    for i in arr:
        seta.add(i)
    arrb = list(map(int,input().split()))
    for i in arrb:
        if i in seta:
            print("YES")
        else:
            print("NO")
        seta.add(i)
