n = int(input())
res = 0
for i in range(n):
    match input():
        case "Tetrahedron":
            res += 4
        case "Cube":
            res += 6
        case "Octahedron":
            res += 8
        case "Dodecahedron":
            res += 12
        case "Icosahedron":
            res += 20
print(res)