N=int(input("N sonini kiriting: N => "))
d=int(input("1-sonni kiriting: n => "))
n=0
k=0
j=0
oldingi=1
l=0
s=1
min = d
for i in range(2,N+1):
    a=int(input(f"{i}-sonni kiriting: n => "))   
    if min<a:
        min=min
        oldingi=1
    else:
        if min==a and oldingi==0:
            min=a
            s=s+1
            oldingi=0
            if n<=s:
                n=s
                j=i
        else:
            min=a
            s=1
            oldingi=0
l=j-n
if (n>=2 and min==d and l==1):
    print(f"To'plamda ketma-ket keluvchi minimumlar soni {n+1} ta");
elif n>=2 and l!=1:
    print(f"To'plamda ketma-ket keluvchi minimumlar soni {n} ta");
else:
    print("To'plamda faqat bitta minimum bor")