l = [2,1,3,4,1,2,1,5,4]
m = l[0]

for i in range(len(l)):
    s = 0
    for j in range(i, len(l)):
        s += l[j]
        if s > m:
            m = s

print(m)
