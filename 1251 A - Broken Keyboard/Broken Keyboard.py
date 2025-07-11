t = int(input())
for i in range(t):
    correct = []
    s = input()
    idx = 0
    while idx != len(s):
        if idx == len(s) - 1:
            correct.append(s[idx])
            idx += 1
        else:
            if s[idx] == s[idx + 1]:
                idx += 2
            else:
                correct.append(s[idx])
                idx += 1
    print("".join(sorted(set(correct)))) 