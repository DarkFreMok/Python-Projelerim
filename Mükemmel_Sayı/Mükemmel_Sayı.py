sayı = int(input("Değer Giriniz:"))

i = 1
toplam = 0

while i < sayı:
    if sayı % i == 0:
        toplam += i
    i += 1
if toplam == sayı:
    print(sayı ,"Mükemmel Sayı.")
else:
    print(sayı ,"Mükemmel Sayı Değildir.")
