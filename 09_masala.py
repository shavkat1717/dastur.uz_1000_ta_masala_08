n=int(input("To'plamning elementlar sonini kiriting: n => "))
b=int(input("To'plamga tegishli 1-sonni kiriting: a => "))
max = b
l=1
j=1
for i in range(2,n+1):
    b=int(input(f"To'plamga tegishli {i}-sonni kiriting: p => "))
    if max<b:
        max=b
        j=i
    if max<=b:
        max=b
        l=i
if l!=j:  
    print(f"\nBirinchi uchragan eng katta element tartibi: {j}.")
    print(f"Oxirgi uchragan eng katta element tartibi: {l}.")
    print("Dastur tugadi")
else:
    print("Birinchi uchragan eng katta element tartibi: ",j)