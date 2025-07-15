n, m = map(int, input().split())
people = []
pairs = []
for i in range(n):
    people.append(input())
for i in range(m):
    a, b = input().split()
    pairs.append((a, b))
max_size = 0
t= None
for i in range(1 << n):
    team = set()
    for j in range(n):
        if (i >> j) & 1:
            team.add(people[j])
    for a, b in pairs:
        if a in team and b in team:
            break
    else:
        if len(team) > max_size:
            max_size = len(team)
            t = team
        
print(max_size)
for el in sorted(t):
    print(el)