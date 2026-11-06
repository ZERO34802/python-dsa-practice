# Problem: Implement a queue (push x / pop / front) using two stacks
# Approach: push onto s1; on pop/front, pour s1 into s2 ONLY when s2 is empty, then use s2's top
# Complexity: amortized O(1) per operation (each element moves s1 -> s2 at most once)
# Mistakes I made:
#   - created st1/st2 but used s1/s2 -> NameError
#   - while loops never decremented (Python has no t--) -> infinite loop
#   - stacks declared outside the test loop -> leftovers carried into the next test case
#   - "push 5" is one line -> input().split(), then parts[0] / int(parts[1])
# Idiom: pouring can be `while s1: s2.append(s1.pop())` because pop() returns the element

tests = int(input())
while tests > 0:
    s1 = []
    s2 = []
    q = int(input())
    while q > 0:
        s = input().split()
        op = s[0]
        if op == "push":
            n = int(s[1])
            s1.append(n)
        else :
            if len(s2) == 0:
                while len(s1) > 0:
                        ele2 = s1[-1]
                        s2.append(ele2)
                        s1.pop()
            if op == "pop":
                if len(s2) > 0:
                    ele = s2[-1]
                    print(ele)
                    s2.pop()
            else:
                print(s2[-1])
        q -= 1
    tests -= 1
