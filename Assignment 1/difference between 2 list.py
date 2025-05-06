a = [1, 2, 3, 4]
b = [2, 4]
d = []
for x in a:
    if x not in b:
        d.append(x)
print(d)
