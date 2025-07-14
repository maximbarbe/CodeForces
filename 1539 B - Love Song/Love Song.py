n, q = map(int, input().split())
s = input()
length = [0]
for c in s:
    length.append(length[-1] + ord(c) - ord('a') + 1)
for j in range(q):
    a, b = map(lambda el:int(el) - 1, input().split())
    print(length[b + 1] - length[a])