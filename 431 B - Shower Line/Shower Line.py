from itertools import permutations
from collections import deque

def score(perm, mat):
    res = 0
    q = deque(perm)
    while q:
        for i in range(0, len(q) - 1, 2):
            res += mat[q[i] - 1][q[i +1] - 1] + mat[q[i+1] - 1][q[i] - 1]
        q.popleft()
    return res
        

perms = [*permutations(range(1, 6))]
m = 0
mat = []
for i in range(5):
    mat.append([*map(int, input().split())])
for p in perms:
    m = max(m, score(p, mat))
print(m)