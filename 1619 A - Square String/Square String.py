t = int(input())
for i in range(t):
    string = input()
    if len(string) % 2 == 1:
        print("NO")
    else:
        print("YES" if string == string[:len(string)//2] * 2 else 'NO')