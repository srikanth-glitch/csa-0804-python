a=int(input("Enter the Number of Elements:"))
l=[]
for i in range(0,a):
    l.append(int(input(f"Enter Value{i+1}:")))
rev=[]
for i in range(-1,-1000,-1):
    t=l[i]
    if t!=l[0]:
        rev.append(l[i])
    else:
        rev.append(l[i])
        break
print(rev)
