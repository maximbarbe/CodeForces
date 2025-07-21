
def ones(s):
    switched = False
    res = 0
    for c in s:
        if c == "0":
            if not switched:
                res += 1
                switched ^= True
        else:
            if switched:
                res += 1
                switched ^= True
    return res

def zeros(s):
    switched = False
    res = 0
    for c in s:
        if c == "0":
            if switched:
                res += 1
                switched ^= True
        else:
            if not switched:
                res += 1
                switched ^= True
    return res


t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    idx = 0
    while idx != n and s[idx] == '0':
        idx += 1
    s = s[idx:]
    print(min(ones(s), zeros(s)))
    