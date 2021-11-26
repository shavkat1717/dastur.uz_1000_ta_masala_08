N=int(input("N sonini kiriting: N => "))
n=0
k=0
j=0
birlar=0
nollar=0
s=0
for i in range(1,N+1):
    a=int(input(f"{i}-sonni kiriting: n => "))   
    if a==1:
        if birlar==1:
            s=s+1
            n=s
            bilar=1
        if n<=s:
            n=s
            j=i
            k=k+1
        if a==0:
            birlar=0
            s=0
if n>=1:
    print(f"To'plamdagi ketma-ket birlar soni {n+1} ta va {j-n} elementdan boshlanadi");
elif k==0:
    print("To'plam faqat 0 lardan iborat");
else:
    print("To'plamdagi ketma-ket birlar mavjud emas")