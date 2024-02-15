print("""****************************
ATM Makinasına Hpş Geldiniz.

İşlemler;

1-Bakiye Sorgulama

2-Para Yatırma

3-Para Çekme 

programdan çıkmak için 'q' ya basın.

****************************
""")
bakiye = 1000
while True:
    işlem = input("İşlem Giriniz:")
    if işlem == "q":
        print("Yine Bekleriz...")
        break
    elif işlem =="1":
        print("Bakiyeniz: {} tl'dir".format(bakiye))

    elif işlem =="2":
        miktar = int(input("Miktarı Giriniz:"))
        bakiye += miktar

    elif işlem =="3":
        miktar2 = int(input("Miktar Giriniz:"))
        if miktar2 > bakiye:
            print("Böyle Bir Miktar Çekemezsiniz...")
            continue
        bakiye -= miktar2
    else:
        print("Geçersiz İşlem.")
