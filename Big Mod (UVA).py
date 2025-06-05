while True:
    b = int(input())
    p = int(input())
    m = int(input())
    print(pow(b, p, m))
    
    try:
        input()
    except:
        break