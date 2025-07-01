from collections import defaultdict



def dfs(prev, node, path):
    for dest in edges[node]:
        if dest == prev:
            continue
        if dest not in removed:
            if dest in path:
                cycles.append(path.copy() + [node, dest])
            else:
                dfs(node, dest, path+ [node])


n,m = map(int, input().split())
edges = defaultdict(lambda:[])
vertices = set()
removed = set()

cycles = []
for i in range(m):
    a, b = map(int, input().split())
    vertices.add(a)
    vertices.add(b)
    edges[a].append(b)
    edges[b].append(a)

res = 0
while True:
    cycles = []
    for vtx in vertices:
        if not vtx in removed:
            dfs(None, vtx, [])
        found = False    
        if len(cycles) != 0:
            for cycle in cycles:
                if len(cycle) % 2 == 0:
                    cycle_vertices = set()
                    found = True
                    res += 1
                    for vtx in cycle:
                        if vtx in cycle_vertices:
                            removed.add(vtx)
                            break
                        cycle_vertices.add(vtx)
                    break
                else:
                    continue
        if found:
            break
    else:
        break
if (n - res)%2 == 1:
    print(res + 1)
else:
    print(res)