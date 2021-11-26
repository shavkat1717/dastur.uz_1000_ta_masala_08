N=int(input("N sonini kiriting: N => "))
j=0
birlar=2
nollar=2
jn=0
jb=0
snollar=0
sbirlar=0
b=0
n=0
for i in range(1,N+1):
    d=int(input(f"{i}-sonni kiriting: n => "))   
    if d==0:
        if nollar==1:
            snollar=snollar+1
        nollar=1
        birlar=2
        if n<=snollar:
            n=snollar
            jn=i
        sbirlar=0
    elif d==1:
        if birlar==1:
            sbirlar=sbirlar+1
        birlar=1
        nollar=2
        if b<=sbirlar:
            b=sbirlar
            jb=i
        snollar=0
if n > b and n!=0:
    print(f"To'plamdagi ketma-ket nollar soni {n + 1} va {jn-n} elementdan boshlanadi");
elif b>n and b!=0:
    print(f"To'plamdagi ketma-ket birlar soni {b + 1}  ta va {jb-b}-elementdan boshlanadi");
elif b==n and b!=0 and n!=0:
    print(f"To'plamdagi ketma-ket birlar va nollar soni bir xil, {b + 1} ta bir va {n+1} ta nol bor, {jn-n} va {jb-b} elementdan boshlanadi");
else:
    print("To'plamdagi ketma-ket birlar yoki nollar mavjud emas");