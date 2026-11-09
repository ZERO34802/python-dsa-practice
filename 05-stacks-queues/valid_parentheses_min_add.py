# Problem: Valid Parentheses (AZ101) - minimum parentheses to add to make S valid
# Approach: stack of unmatched '('; an unmatched ')' needs one added '(' (ans += 1);
#   leftover '(' on the stack each need a ')' (ans += len(st))
# Complexity: O(|S|)
# Mistakes I made:
#   - popped from an EMPTY stack in the unmatched-')' branch -> IndexError; just ans += 1
# Got right: input().strip() - with sys.stdin.readline the line keeps '\n', which would count as a ')'
# Idioms for next time: for c in s; if st:; ans += len(st) needs no if
#   (a plain counter of open '(' would also replace the stack)

import sys
input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    s = input().strip()
    st = []
    n = len(s)
    ans = 0
    for i in range(0,n):
        if s[i] == '(':
            st.append('(')
        else :
            if len(st) > 0:
                st.pop()
            else :
                ans += 1
    if len(st) > 0:
        ans += len(st)
    out.append(ans)
print("\n".join(map(str,out)))
