n=int(input("To'plamning elementlar sonini kiriting: n => "))
a=int(input("To'plamga tegishli 1-sonni kiriting: a => "))
min = a
l=1
j=1
for i in range(2,n+1):
    a=int(input(f"To'plamga tegishli {i}-sonni kiriting: p => "))
    if min>a:
        min=a
        j=i
    elif min>=a:
        min=a
        l=i
if l!=j:  
    print(f"\nBirinchi uchragan eng kichik element tartibi: {j}.")
    print(f"Oxirgi uchragan eng kichik element tartibi: {l}.")
    print("Dastur tugadi")