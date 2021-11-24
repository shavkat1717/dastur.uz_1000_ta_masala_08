n=int(input("Jami nechta sonlar juftligini solishtirmoqchisiz: n => "))
print("1-juftlikning parametrlarini kiriting:")
m=int(input("massa => "))
v=int(input("hajm => "))
p = m/v
max = p
l=1
for i in range(2,n+1):
    print(f"\n{i}-juftlikning parametrlarini kiriting:")
    m=int(input("massa => "))
    v=int(input("hajm => "))
    p = m/v
    if max<p:
        max=p
        l=i
print(f"\nEng katta zichlik: {max} ya'ni {l}-juftlik.")
print("Dastur tugadi")