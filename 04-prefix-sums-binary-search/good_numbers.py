# Problem: Good Numbers - N ranges [l, r]; a number is good if at least K ranges cover it.
#   Q queries: how many good numbers in [L, R]?
# Approach: difference array (v[l] += 1, v[r+1] -= 1) -> prefix sum = coverage per number;
#   second prefix sum over (coverage >= K) answers each query as pref2[R] - pref2[L-1]
# Complexity: O(N + MAX + Q), MAX = 1e6
# Mistakes I made:
#   - map(int.input()) -> AttributeError; it's map(int, input().split())
#   - v sized 1000001 -> v[r+1] with r = 1e6 is out of range (IndexError); size it 1000002
# Fast I/O (N, Q up to 1e6): input = sys.stdin.readline, collect answers in a list, print once with join
# Ternary: curr = 1 if cond else 0  (Python has no ? :), or int(cond)

import sys
input = sys.stdin.readline

n,k,q = map(int,input().split())
v = [0]*(1000002)
pref = [0]*(1000002)
pref2 = [0]*(1000002)
for _ in range(n):
    l,r = map(int,input().split())
    v[l] += 1
    v[r + 1] -= 1
for i in range(1,1000001):
    pref[i] = pref[i - 1] + v[i]
for i in range(1,1000001):
    curr = 1 if pref[i] >= k else 0
    pref2[i] = pref2[i - 1] + curr
out = []
for _ in range(q):
    l,r = map(int,input().split())
    out.append(pref2[r] - pref2[l - 1])
print("\n".join(map(str,out)))
