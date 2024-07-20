n = int(input())
p, *x_vals = map(int, input().split())
q, *y_vals = map(int, input().split())
if len(set(x_vals).union(set(y_vals))) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")