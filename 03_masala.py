n=int(input("Jami to'g'ri to'rtburchaklarning sonini kiriting n => "))
print("1-to'g'ri to'rtburchakning tomonlarini:")
x=int(input("a => "))
y=int(input("b => "))
p = 2*(x+y)
min = p
l=1
for i in range(2,n+1):
    print(f"\n{i}-to'g'ri to'rtburchakning tomonlarini:")
    x=int(input("a => "))
    y=int(input("b => "))
    p = 2*(x+y)
    if min>p:
        min=p
        l=i
print(f"\nminimum perimetr: {min} ya'ni: {l}-to'g'ri to'rtburchak")
print("\nDastur tugadi")