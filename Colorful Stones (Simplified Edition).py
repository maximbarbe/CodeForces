stones = input()
string = input()
cur = 0
for i in range(len(string)):
    if cur != len(stones) and stones[cur] == string[i]:
        cur += 1
        
else:
    print(cur + 1)