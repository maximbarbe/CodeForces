t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if s.startswith("2020") or (s.startswith("202") and s.endswith("0")) or (s.startswith("20") and s.endswith("20")) or (s.startswith("2") and s.endswith("020")) or s.endswith("2020"):
        print("YES")
    else:
        print("NO")