a=int(input("Enter Number of Elements:"))
l=[]
for i in range(a):
    l.append(int(input()))
lar=l[0]
for i in l:
    if i>=lar:
        lar=i
print(lar)
lar2=l[0]
for i in l:
    if i<lar:
        if i>=lar2:
            lar2=i
print(lar2)
