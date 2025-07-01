# Probleme DP (possiblement)
# On y va de l'arrière vers l'avant
# Pour un arbre i, si on peut le couper et dans quelle direction on veut le couper dépend de l'arbre i + 1 et i - 1
# dp[0] -> On ne coupe pas l'arbre
# dp[1] -> On coupe l'arbre vers la gauche
# dp[2] -> On coupe l'arbre vers la droite
from math import inf

n = int(input())
v = [(-inf, 0)]
for i in range(n):
    xi, hi = map(int, input().split())
    v.append((xi, hi))
v.append((inf, 0))
dp = [[0 for i in range(n + 2)] for j in range(3)]
for i in range(n, 0, -1):
    
    x, h = v[i]
    x_prev, h_prev = v[i - 1]
    x_next, h_next = v[i + 1]
    dp[0][i] = max(dp[0][i + 1], dp[1][i + 1], dp[2][i + 1])
    if x - h <= x_prev:
        dp[1][i] = 0
    else:
        dp[1][i] = 1 + max(dp[0][i + 1], dp[1][i + 1], dp[2][i + 1])
    if x + h >= x_next:
        dp[2][i] = 0
    else:
        if x + h >= x_next - h_next:
            dp[2][i] = 1 + max(dp[0][i + 1], dp[2][i + 1])
        else:
            dp[2][i] = 1 + max(dp[0][i + 1],dp[1][i + 1], dp[2][i + 1])
print(max(dp[0][1], dp[1][1], dp[2][1]))