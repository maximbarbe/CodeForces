def generates(step, mod):
    seen = set()
    x = 0
    while True:
        if len(seen) == mod:
            return True
        x = (x + step)%mod
        if x in seen:
            return False
        seen.add(x)

while True:
    try:
        step, mod = map(int, input().split())
        res = ""
        if generates(step, mod):
            res = "Good Choice"
        else:
            res = "Bad Choice"
        print(str(step).rjust(10)+str(mod).rjust(10)+"    "+res)    
        print()
    except:
        break