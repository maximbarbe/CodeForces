string = input().lstrip("{").rstrip("}").replace(" ", "").split(",")
if string[0] == "":
    print(0)
else:
    print(len(set(string)))