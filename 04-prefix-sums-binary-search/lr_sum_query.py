# Problem: LR Sum Query - Q queries of (A[L] + ... + A[R]) mod 1e9+7, 1-indexed, A[i] can be negative
# Approach: prefix sums mod M; answer = pref[R] - pref[L-1] (mod M)
# Complexity: O(N + Q)
# Mistakes I made:
#   - pref[l-1] in 0-indexed form INCLUDES A[L] -> off by one; convert L, R to 0-indexed first
#   - stored (pref[i-1]%M + arr[i]%M) without a final % M -> values up to 2M-2 printed raw (WA)
#   - TLE with plain input() at N, Q = 1e6 -> sys.stdin.readline (enough here; batching output helps further)
# Notes:
#   - Python % with positive M is never negative: (a - b) % M needs no + M like C++
#   - cleaner: 1-indexed pref with pref[0] = 0, then every query is pref[r] - pref[l-1], no special case

import sys
input = sys.stdin.readline

M = 1000000007

n, q = map(int,input().split())
arr = list(map(int,input().split()))
pref = [0]*(n + 1)
pref[0] = arr[0]%M
for i in range(1,n):
    pref[i] = (pref[i - 1]%M + arr[i]%M)%M
for _ in range(q):
    l, r = map(int,input().split())
    l -= 1
    r -= 1
    if l == 0:
        print(pref[r])
    else:
        diff = (pref[r]%M - pref[l - 1]%M)%M
        print(diff)
