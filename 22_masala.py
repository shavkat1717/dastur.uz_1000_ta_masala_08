n=int(input("N sonini kiriting: N => "))
a=int(input("1-sonini kiriting: n => "))
b=int(input("2-sonini kiriting: n => "))
if a>b:
    min1=b
    min2=a
else:
    min1=a
    min2=b
for i in range(3,n+1):
    c=int(input(f"{i}-sonni kiriting: n => "))    
    if min1>c:
        min2=min1
        min1=c
    elif min2>c:
        min2=c
        min1=min1
print(f"Eng minimum son: min1 = {min1};")
print(f"Undan keyingi eng minimum son: min2={min2}.")