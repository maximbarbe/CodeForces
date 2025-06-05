n = int(input())
v = [*map(int, input().split())]
increasing = True
increase_again = False
start = end = None
maximum = 0
for i in range(1, n):
    if v[i] < v[i - 1]:
        if increase_again:
            print("no")
            exit()
        if start == None:
            start = i - 1
            increasing = False
            maximum = v[start]
    else:
        if not increasing and not increase_again:
            if maximum > v[i]:
                print("no")
                exit()
            end = i - 1
            increase_again = True

if start == None:
    start = end = 0
elif end == None:
    end = n-1
sorted_vals = v[:start] + sorted(v[start:end + 1]) + v[end+1:]
if sorted_vals == sorted(v):
    print("yes")
    print(start +1, end + 1)
else:
    print("no") 
