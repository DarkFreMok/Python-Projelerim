print("""*****************************
Kullanıcı Girdi Aldısı

Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırılır.
*****************************
""")
toplam = 0

while True:
    sayı = input("Değer Giriniz:")
    if sayı == "q":
        break
    sayı = int(sayı)
    toplam += sayı
    print("Girdiğiniz Sayıların Toplamı:",toplam)
