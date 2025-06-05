from math import gcd, comb, sqrt

while True:
    n = int(input())
    if n == 0:
        break
    nums = []
    for i in range(n):
        nums.append(int(input()))
    pairs = 0
    denum = comb(n, 2)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if gcd(nums[i], nums[j]) == 1:
                pairs += 1
    if pairs == 0:
        print("No estimate for this data set.")
    else:
        approx = sqrt(denum * 6/pairs)
        print("{0:.6f}".format(approx))