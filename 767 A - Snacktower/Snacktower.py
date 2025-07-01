from collections import defaultdict

n = int(input())
order = [*map(int, input().split())]
seen = defaultdict(lambda:False)
days = []
cur = n
current_day = []
for v in order:
    seen[v] = True
    if v != cur:
        days.append(current_day)
        current_day = []
    else:
        while seen[cur] and cur != 0:
            current_day.append(cur)
            cur -= 1
        days.append(current_day)
        current_day = []

        
if len(current_day)!=0:
    days.append(current_day)
for i in range(len(days)):
    if len(days[i]) == 0:
        print()
    else:
        print(*days[i])
