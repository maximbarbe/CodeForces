n = int(input())
alice = bob = 0
left = 0
right = n-1
vals = [*map(int, input().split())]
while left <= right:
    if left == right:
        alice += 1
        break
    else:
        if vals[left] == vals[right]:
            left += 1
            alice += 1
            right -= 1
            bob += 1
        elif vals[left] < vals[right]:
            vals[right] -= vals[left]
            left += 1
            alice += 1
            if left == right:
                bob += 1
                break
        elif vals[left] > vals[right]:
            vals[left] -= vals[right]
            right -= 1
            bob += 1
            if left == right:
                alice += 1
                break
print(alice, bob)