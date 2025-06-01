n = int(input())
priority = {
    "rat": 0,
    "woman": 1,
    "child": 1,
    "man": 2,
    "captain":3
}
people = []
for i in range(n):
    name, status = input().split()
    people.append((name, status, i))
people.sort(key=lambda el:(priority[el[1]], el[2]))
for x, _, _1 in people:
    print(x)