n, m, a = map(int, input().split())

horizontal = m // a + 1 if m %a != 0 else m //a
vertical = n // a + 1 if n % a != 0 else n //a
print(horizontal * vertical)