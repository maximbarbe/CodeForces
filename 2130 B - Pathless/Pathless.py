t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    squares = [*map(int, input().split())]
    if sum(squares) > s:
        print(*squares)
    else:
        cnt = [0, 0, 0]
        for i in range(len(squares)):
            cnt[squares[i]] += 1
        need = s - cnt[1] - 2*cnt[2]
        if need % 2 == 0 or need >= 3:
            print(-1)
        else:
            if need == 1:
                res = [0]*cnt[0] + [2]*cnt[2] + [1]*cnt[1]
            
            print(*res)                