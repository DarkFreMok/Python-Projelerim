print("""*********************
Sınav Notu Ortalaması
*********************""")
a = int(input("İlk Vize Sınavınızı Giriniz:"))
b = int(input("İkinci Vize Sınavınızı Giriniz:"))
c = int(input("Final Sınavınızı Giriniz:"))
Vıze1 = a * 45/ 100
Vıze2 = b * 5 / 100
Fınal = c * 50/ 100
ToplamNote = (Vıze1 + Vıze2 + Fınal)

if ToplamNote >= 90:
    print("AA")
elif ToplamNote >= 85:
    print("BA")
elif ToplamNote >= 80:
    print("BB")
elif ToplamNote >= 75:
    print("CB")
elif ToplamNote >=70:
    print("CC")
elif ToplamNote >=65:
    print("DC")
elif ToplamNote >=60:
    print("DD")
elif ToplamNote >=55:
    print("FD")
else:
    print("FF")

print("Sonuç:", ToplamNote)
