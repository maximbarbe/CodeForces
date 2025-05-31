t =int(input())
for i in range(t):
    input()
    xll1, yll1, xur1, yur1 = map(int, input().split())
    xll2, yll2, xur2, yur2 = map(int, input().split())
    if xll1 >= xur2 or xur1 <= xll2 or yll1 >= yur2 or yur1 <= yll2:
        print("No Overlap")
    else:
        print(max(xll1, xll2), max(yll1, yll2), min(xur1, xur2), min(yur1, yur2))
    if i != t-1:
        print()