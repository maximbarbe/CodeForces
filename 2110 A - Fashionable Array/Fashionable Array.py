t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    vals.sort()
    f_even = f_odd = None
    l_even = l_odd = None
    for i in range(len(vals)):
        if vals[i] %2 == 0:
            if f_even == None:
                f_even = i
        else:
            if f_odd == None:
                f_odd = i
    for i in range(len(vals) -1, -1, -1):
        if vals[i] %2 == 0:
            if l_even == None:
                l_even = i
        else:
            if l_odd == None:
                l_odd = i
    if f_even != None and f_odd != None:
        print(min(f_even + (n-(l_even + 1)), f_odd + (n-(l_odd + 1))))
    elif f_even != None:
        print(f_even + (n-(l_even + 1)))
    else:
        print(f_odd + (n-(l_odd + 1)))