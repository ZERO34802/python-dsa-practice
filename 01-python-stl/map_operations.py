# Problem: Map queries - add x y / erase x / print x (print 0 if missing)
# Approach: plain dict; `in` to check keys, del to erase
# Complexity: O(1) average per query
# Mistakes I made:
#   - wrote `else if` -> Python uses `elif` (syntax error)
#   - print branch checked s[0] (the word "print") instead of the key s[1]
# Habit to build: convert tokens with int(s[1]); strings only worked here because
# the judge needed exact matches ("10" < "9" is True for strings)

t = int(input())
for _ in range(1,t + 1):
    q = int(input())
    mp = {}
    for _ in range(1,q + 1):
        s = input().split()
        if s[0] == "add":
            x = s[1]
            y = s[2]
            mp[x] = y
        elif s[0] == "erase":
            x = s[1]
            if x in mp:
                del mp[x]
        elif s[0] == "print":
            if s[1] in mp:
                print(mp[s[1]])
            else :
                print(0)
