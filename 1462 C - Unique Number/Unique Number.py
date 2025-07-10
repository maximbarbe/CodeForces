t = int(input())
for i in range(t):
    n = int(input())
    if n <= 9:
        print(n)
    else:
        match n:
            case 10:
                print(19)
            case 11:
                print(29)
            case 12:
                print(39)
            case 13:
                print(49)
            case 14:
                print(59)
            case 15:
                print(69)
            case 16:
                print(79)
            case 17:
                print(89)
            case 18:
                print(189)
            case 19:
                print(289)
            case 20:
                print(389)
            case 21:
                print(489)
            case 22:
                print(589)
            case 23:
                print(689)
            case 24:
                print(789)
            case 25:
                print(1789)
            case 26:
                print(2789)
            case 27:
                print(3789)
            case 28:
                print(4789)
            case 29:
                print(5789)
            case 30:
                print(6789)
            case 31:
                print(16789)
            case 32:
                print(26789)
            case 33:
                print(36789)
            case 34:
                print(46789)
            case 35:
                print(56789)
            case 36:
                print(156789)
            case 37:
                print(256789)
            case 38:
                print(356789)
            case 39:
                print(456789)
            case 40:
                print(1456789)
            case 41:
                print(2456789)
            case 42:
                print(3456789)
            case 43:
                print(13456789)
            case 44:
                print(23456789)
            case 45:
                print(123456789)
            case _:
                print(-1)