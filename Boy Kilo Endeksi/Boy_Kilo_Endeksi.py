print("""********************
Kullanıcı Kilo/Boy Endeksi
********************""")
a = float(input("Kullanıcı Boyunu Giriniz:"))
b = int(input("Kullanıcı Kilosunu Giriniz:"))
BKİ= b/(a*a)
if BKİ <= 18.5:
    print("Zayıf")
elif BKİ <=25:
    print("Normal")
elif BKİ <= 30:
    print("Fazla Kilolu")
elif BKİ > 30:
    print("Obez")
