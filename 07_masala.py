n=int(input("To'plamning elementlar sonini kiriting: n => "))
a=int(input("To'plamga tegishli 1-sonni kiriting: a => "))
max = a
min = a
l=1
j=1
for i in range(2,n+1):
    a=int(input(f"To'plamga tegishli {i}-sonni kiriting: a => "))
    if max<a:
        max=a
        l=i
    elif min>=a:
        min=a
        j=i
print(f"\nBirinchi uchragan eng katta element tartibi: {l}.")
print(f"Oxirgi uchragan eng kichik element tartibi: {j}.")
print("Dastur tugadi")