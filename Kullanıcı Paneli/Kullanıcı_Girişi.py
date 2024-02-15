print("""
******************************
Kullanıcı Girişi
******************************
""")
sys_adı = "FreMok"
sys_şifre ="LH44"
giriş_hakkı = 3

while True:
    Kullanıcı_Adı = input("Kullancı Adını Giriniz:")
    Kullanıcı_şifre = input("Kullanıcı Şifre Giriniz:")
    if Kullanıcı_Adı != sys_adı and Kullanıcı_şifre == sys_şifre:
        print("Kullancı Adı Yanlış...")
        giriş_hakkı -=1
    elif Kullanıcı_Adı == sys_adı and Kullanıcı_şifre != sys_şifre:
        print("Kullancı Şifre Yanlış...")
        giriş_hakkı -=1
    elif Kullanıcı_Adı != sys_adı and Kullanıcı_şifre != sys_şifre:
        print("Kullancı Adı Ve Şifre Hatalıdır...")
        giriş_hakkı -=1
    else:
        print("Sistem Doğrulandı.")
        break
    if giriş_hakkı ==0:
        print("Giriş Hakkınız Bitti.")
        break
