from collections import defaultdict

edges = {
    "A": [],
    "B": [],
    "C": []
}
in_deg = {
    "A": 0,
    "B": 0,
    "C": 0
}
for i in range(3):
    s = input()
    first = s[0]
    sec = s[2]
    sign = s[1]
    if sign == ">":
        edges[first].append(sec)
        in_deg[sec] += 1
    else:
        edges[sec].append(first)
        in_deg[first] += 1
for k, v in in_deg.items():
    if v == 0:
        heaviest = k
        if len(edges[k]) == 2:
            for v2 in edges[heaviest]:
                if edges[v2]:
                    print(f"{edges[v2][0]}{v2}{heaviest}")
        else:
            print(f"{edges[edges[k][0]][0]}{edges[k][0]}{k}")
        exit()
else:
    print("Impossible")
    