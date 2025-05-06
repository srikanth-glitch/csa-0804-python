a = [1, 2, 3]
b = [2, 3, 4]
c = []

for x in a:
    if x in b and x not in c:
        c.append(x)

print(c)
