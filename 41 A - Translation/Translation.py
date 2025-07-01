first = input()
sec = input()
if len(first) != len(sec):
    print("NO")
else:
    for i in range(len(first)):
        if first[i] != sec[len(sec) - i - 1]:
            print("NO")
            break
    else:
        print("YES")