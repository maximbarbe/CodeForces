

def find(s, idx):
    global string,res,f
    if idx == len(string):
        if f(s) and s > res:
            res = s
        return
    find(s, idx + 1)
    find(s + string[idx], idx + 1)


f = lambda x:x==x[::-1]
string = input()
res=""
find("", 0)
print(res)