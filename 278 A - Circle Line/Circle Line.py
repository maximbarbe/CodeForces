n = int(input())
distances = [*map(int, input().split())]
s, t = map(lambda el:int(el) -1, input().split())
right = 0
cur = s
while cur != t:
    right += distances[cur]
    cur = (cur + 1)%n
left = 0
cur = s - 1
while cur != t:
    left += distances[cur]
    cur = (cur - 1)%n
print(min(right, left + distances[t]))