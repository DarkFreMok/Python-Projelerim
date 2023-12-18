print("""*******************
Kullanıcının Seçtiği En Büyüğünü Alma
*******************""")
a = int(input("Birinici Değer:"))
b= int(input("İkinci Değer:"))
c= int(input("Üçüncü Değer:"))
if (a > (b and c)):
    print("En Büyük Değer:",a)
elif(b > (a and c)):
    print("En Büyük Değer:",b)
else:
    print("En Büyük Değer:",c)
