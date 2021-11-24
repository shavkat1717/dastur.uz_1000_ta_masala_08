n=int(input("To'plamning elementlar sonini kiriting n => "))
a=int(input("Ushbu to'plamning 1-elementini kiriting: a => "))
min = a
max = a
for i in range(2,n+1):
    a=int(input(f"{i}-elementni kiriting: x => "))
    if max<a:
        max=a
    if min>a:
        min=a
print(f"\nTo'plamning minimum qiymati: {min}")
print(f"To'plamning maksimum qiymati: {max}")
print("\nDastur tugadi")