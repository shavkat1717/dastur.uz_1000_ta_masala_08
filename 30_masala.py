N=int(input("N sonini kiriting: N => "))
d=int(input("1-sonni kiriting: n => "))
k=0
j=0
s=1
oldingi=1
l=0
nmax=N
max = d
for i in range(2,N+1):
    a=int(input(f"{i}-sonni kiriting: n => "))   
    if max>a:
        if nmax>=s:
            nmax=s
        oldingi=0
    else:
        if max==a and oldingi==1:
            s=s+1
            oldingi=1
        elif max<a:
            max=a
            s=1
            oldingi=1
if max<s:
    print(nmax);
else:
    print(s)