import sys

res = 0
participants = 0

for line in sys.stdin:
    line = line.rstrip()
    match line[0]:
        case "+":
            participants += 1
        case "-":
            participants -= 1
        case _:
            message = line.split(":")[1]
            res += len(message) * participants
print(res)
        