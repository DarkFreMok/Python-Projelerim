print("""*******************************
Faktöriyel Bulma Programı

Çıkmak için 'q'ya basın.

*******************************
""")

while True:
    kullanıcı_değer = input("Bir Değer Giriniz:")
    if kullanıcı_değer =="q":
        print("İşlem Sonlanıyor...")
        break
    else:
        sayı = int(kullanıcı_değer)

        faktöriyel_değişken = 1

        for i in range(2,sayı+1):
            faktöriyel_değişken *= i 
            print("Faktöriyel:",faktöriyel_değişken)
