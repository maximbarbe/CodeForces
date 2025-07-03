t = int(input())
for i in range(t):
    s = input()
    chars = []
    added = False
    for c in s:
        if added:
            chars.append(c)
            continue
        if chars and c == chars[-1]:
            chars.append(chr((ord(c) - ord('a') + 1)%26 + ord('a')))
            chars.append(c)
            added=True
        else:
            chars.append(c)
    if not added:
        print(chr((ord(s[0]) - ord('a') + 1)%26 + ord('a'))+s)
    else:        
        print("".join(chars))