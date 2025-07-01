# Probablement dynamic programming
# Aller de l'arrière vers l'avant
# Dépend du choix que l'on a fait à la journée d'après et de l'option pour la journée
# 
# Si ai = 0 -> Peu importe ce qu'on a fait, on doit prendre une journée de repos
# Si ai = 1 -> Journée de repos ou contest
# Si ai = 2 -> Journée de repos ou sport
# Si ai = 3 -> Journée de repos, sport ou contest
# dp[0] = sport
# dp[1] = contest
# dp[2] = repos
# dp[i][j], je fais l'activité i au jour j
from math import inf
n = int(input())
dp = [[inf for i in range(n + 1)] for j in range(3)]
v = [*map(int, input().split())]
dp[0][n] = 0
dp[1][n] = 0
dp[2][n] = 0

    
for i in range(n -1, -1, -1):
    dp[2][i] = 1 + min(dp[0][i + 1], dp[1][i + 1], dp[2][i + 1])
    if v[i] == 1:
        dp[1][i] = min(dp[0][i + 1], dp[2][i + 1])
    elif v[i] == 2:
        dp[0][i] = min(dp[1][i + 1], dp[2][i + 1])
    elif v[i] == 3:
        dp[0][i] = min(dp[1][i + 1], dp[2][i + 1])
        dp[1][i] = min(dp[0][i + 1], dp[2][i + 1])
print(min(dp[0][0], dp[1][0], dp[2][0]))