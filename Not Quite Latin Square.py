t = int(input())
for i in range(t):
    seen = {
        'A': 0,
        'B': 0,
        'C': 0
    }
    for j in range(3):
        row = input()
        for char in row:
            if char != "?":
                seen[char] += 1
    for key in seen.keys():
        if seen[key] != 3:
            print(key)
            break
