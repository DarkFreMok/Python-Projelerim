import math

def hesap_makinesi():
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Üs Alma")
    print("6. Karekök Alma")
    print("7. Sinüs Hesaplama")
    print("8. Cosinüs Hesaplama")
    print("9. Tanjant Hesaplama")
    print("Çıkış için q ya basınız")

    while True:
        secim = input("Yapmak istediğiniz işlemi seçin (1-9): ")
        if secim == "q" :
            break

        if secim in ['1', '2', '3', '4']:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        elif secim in ['5', '6']:
             sayi = float(input("Bir sayı girin: "))
        else:
            aci = float(input("Açıyı derece cinsinden girin: "))

        if secim == '1':
            print("Sonuç:", sayi1 + sayi2)
        elif secim == '2':
            print("Sonuç:", sayi1 - sayi2)
        elif secim == '3':
            print("Sonuç:", sayi1 * sayi2)
        elif secim == '4':
            print("Sonuç:", sayi1 / sayi2)
        elif secim == '5':
            print("Sonuç:", math.pow(sayi, 2))
        elif secim == '6':
            print("Sonuç:", math.sqrt(sayi))
        elif secim == '7':
            print("Sonuç:", math.sin(math.radians(aci)))
        elif secim == '8':
            print("Sonuç:", math.cos(math.radians(aci)))
        elif secim == '9':
            print("Sonuç:", math.tan(math.radians(aci)))
        else:
            print("Geçersiz seçim!")

hesap_makinesi()
