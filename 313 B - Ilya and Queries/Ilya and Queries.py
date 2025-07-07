s = input()
equal = [False]*len(s)
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        equal[i] = True
prefix = [0]*(len(s) + 1)
for i in range(len(equal)):
    prefix[i + 1] = prefix[i] + int(equal[i])
q = int(input())
for i in range(q):
    a, b = map(lambda el:int(el) -1, input().split())
    print(prefix[b] - prefix[a])