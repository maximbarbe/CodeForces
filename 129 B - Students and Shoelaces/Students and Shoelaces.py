n, m = map(int, input().split())
kicked = dict()
students = dict()
for i in range(n):
    kicked[i] = False
    students[i] = set()
    
for i in range(m):
    v1, v2 = map(lambda el: int(el) - 1, input().split())
    students[v1].add(v2)
    students[v2].add(v1)
res = 0
while True:
    to_remove = set()
    for key in students.keys():
        if not kicked[key] and len(students[key]) == 1:
            to_remove.add(key)
    for key in to_remove:
        for el in list(students[key]):
            students[el].remove(key)
        kicked[key] = True
    if len(to_remove) == 0:
        break
    res += 1       
print(res)