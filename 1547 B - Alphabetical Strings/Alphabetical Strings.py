def is_alphabetical(s: str):
    try:
        left = right = s.index("a")
    except:
        return False
    left -= 1
    right += 1
    for i in range(1, len(s)):
        c = chr(ord('a') + i)
        if left != -1 and s[left] == c:
            left -= 1
        elif right != len(s) and s[right] == c:
            right += 1
        else:
            return False
    
    
    if left == -1 and right == len(s):
        return True
    return False
        
for i in range(int(input())):
    print(("NO", "YES")[is_alphabetical(input())])