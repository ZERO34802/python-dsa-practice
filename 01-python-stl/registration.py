# Problem: Registration (AZ101) - print OK on first registration, else name + times registered before
# Approach: defaultdict(int) count per name; print before incrementing
# Complexity: O(sum of N) average
# Mistakes I made:
#   - mp[s]++ -> Python has no ++ (syntax error); use mp[s] += 1
#   - first version only incremented on the first registration -> abc1 printed twice instead of abc1, abc2
# Idiom: both branches increment, so `mp[s] += 1` can sit once after the if/else
# Note: `s in mp` on a defaultdict checks without inserting; print(s, mp[s], sep="") prints harry1

from collections import defaultdict

t = int(input())
for _ in range(t):
    mp = defaultdict(int)
    n = int(input())
    for _ in range(n):
        s = input()
        if s in mp:
            print(s,mp[s],sep="")
            mp[s]+=1
        else:
            mp[s] += 1
            print("OK")
