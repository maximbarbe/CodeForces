from math import lcm

for i in range(int(input())):
    s1 = input()
    s2 = input()
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    v1 = len(s1)
    v2 = len(s2)
    l = lcm(v1, v2)
    if s1*(l//v1) == s2*(l//v2):
        print(s1*(l//v1))
    else:
        print(-1)