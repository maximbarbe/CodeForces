
for i in range(int(input())):
    minimum = 200_001
    c = {"1":0, "2": 0, "3": 0}
    s = input()
    left = right = 0
    while right != len(s):
        c[s[right]] += 1
        if min(c.values()) >= 1:
            minimum = min(minimum, right - left + 1)
        right += 1
        while c[s[left]] > 1:
            c[s[left]] -= 1
            left += 1
        if min(c.values()) >= 1:
            if right == len(s):
                minimum = min(minimum, right - left)
            else:
                minimum = min(minimum, right - left)
    if minimum == 200_001:
        print(0)
    else:
        print(minimum)