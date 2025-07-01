n = int(input())
for i in range(n//2 + 1):
    n_ds = 2*i + 1
    n_stars = (n - n_ds)//2
    print("*"*n_stars + "D"*n_ds + "*"*n_stars)
for i in range(n//2):
    n_ds = n - 2*(i+1)
    n_stars = (n - n_ds)//2
    print("*"*n_stars + "D"*n_ds + "*"*n_stars)