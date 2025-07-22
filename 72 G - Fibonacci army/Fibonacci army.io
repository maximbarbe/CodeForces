n := File standardInput readLine asNumber

f := List clone append(1, 1)
for(i, 2, 20, f append(f at(f size - 1) + f at(f size - 2)))
writeln(f at (n))