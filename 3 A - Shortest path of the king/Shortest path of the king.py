from collections import defaultdict, deque
 
 
s = input()
t = input()
s = (8-int(s[1]), ord(s[0]) - ord('a'))
t = (8-int(t[1]), ord(t[0]) - ord('a'))
 
moves = defaultdict(lambda:None)
q = deque([s])
while q:
    x, y = q.popleft()
    if (x, y) ==t:
        break
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if 0 <= x + dx < 8 and 0 <= y + dy < 8 and moves[(x + dx, y+dy)] == None and (x+dx, y+dy) != s:
            q.append((x+dx, y+dy))
            moves[(x+dx, y+dy)] = (dx, dy)
 
path = []
cur = t
while moves[cur] != None:
    path.append(moves[cur])
    cur = (cur[0] - moves[cur][0], cur[1] - moves[cur][1])
for i, (x,y) in enumerate(path):
    match (x, y):
        case (0, 1):
            path[i] = "R"
        case (0, -1):
            path[i] = "L"
        case (1, 0):
            path[i] = "D"
        case (-1, 0):
            path[i] = "U"
        case (1,1):
            path[i] = 'RD'
        case (1, -1):
            path[i] = "LD"
        case (-1, 1):
            path[i] = "RU"
        case (-1, -1):
            path[i] = "LU"
print(len(path))
for m in path:
    print(m)