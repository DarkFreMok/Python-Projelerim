print("""******************************
Tam Bölen Bulma
******************************
""")
def tambolenbulma(sayı):
    tam_bölen = []
    for i in range(2,sayı):

        if sayı % i == 0:
            tam_bölen.append(i)
    return  tam_bölen
while True:
    sayı = input("Değer Giriniz:")
    if sayı == 'q':
        print("Program Sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)
        print("Tam Bölenler",tambolenbulma(sayı))
