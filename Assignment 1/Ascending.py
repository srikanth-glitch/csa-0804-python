a = [2, 4, 8, 5, 1, 3, 6, 7]
n = len(a)
for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j] 

print(a)
