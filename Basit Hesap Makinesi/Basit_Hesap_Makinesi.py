print("""***********************************
Hesap Makinesi Programı
1.Toplama İşlemi

2.Çıkarma İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi
***********************************""")
işlem = input("İşlem giriniz:")

a = int(input("Birinci Sayı :"))
b = int(input("İkinci Sayı:"))

if işlem == "1":
    print("{} ile {} in toplama {} dir".format(a,b,a+b))
elif işlem == "2":
    print("{} ile {} in çıkarma {} dir".format(a, b, a-b))
elif işlem == "3":
    print("{} ile {} in çarpma {} dir".format(a,b,a*b))
elif işlem == "4":
    print("{} ile {} in bölme {} dir".format(a,b,a/b))
else:
    print("Geçersiz İşlem.....")
