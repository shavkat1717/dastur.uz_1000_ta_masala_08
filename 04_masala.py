n=int(input("To'plam elementlari sonini kiriting n => "))
a=int(input("To'plamning 1-elementini kiriting: a => "))
min = a
l=1
for i in range(2,n+1):
    a=int(input(f"To'plamning {i}-elementini kiriting: a => "))
    if min>a:
        min=a
        l=i
print(f"\nminimum elementning tartib raqami: {l}")
print("\nDastur tugadi")