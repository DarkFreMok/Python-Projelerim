print("""********************
Kullanıcı Giriş
********************""")
Adı = "FreMok"
parola = "LH44"

Kullanıcı_adı = input("Kullanıcı Adı:")
Kullanıcı_parola = input("Kullanıcı Parola:")

if Adı == Kullanıcı_adı and parola != Kullanıcı_parola:
    print("Parola Hatalı!")
elif Adı != Kullanıcı_adı and parola == Kullanıcı_parola:
    print("Kullanıcı Adı Hatalı")
elif Adı != Kullanıcı_adı and parola != Kullanıcı_parola:
    print("Kullanıcı Adı Ve Parola Hatalı")
else:
    print("Sisteme Başarıyla Giriş Yaptınız.")
