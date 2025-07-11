from math import ceil

t = int(input())
for i in range(t):
    n,m,k = map(int, input().split())
    # S'il y a moins (ou égal) de jokers qu'il y a de cartes dans une main, on peut donner tous les jokers à quelqu'un
    if m <= n//k:
        print(m)
    else:
        # Sinon, une personne obtient n//k jokers, il y a donc m - n//k jokers dans les n-n//k autres cartes à distribuer aux k-1 autres personnes
        
        c = n//k
        n -= c
        m -= c
        max_other = ceil(m/(k-1))
        print(c - max_other)