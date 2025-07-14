for i in range(int(input())):
    s = input()
    print(("NO", "YES")[s.count("A") + s.count("C")==s.count("B")])