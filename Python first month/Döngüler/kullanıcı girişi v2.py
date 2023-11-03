print("""
************************
Kullanıcı Girişi
************************
""")
sys_kullanıcı_adı = "uzayoc"
sys_parola = "123123"
giriş_hakkı = 3
while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola:
        print("Lütfen kullanıcı adını kontrol ediniz......")
        giriş_hakkı -=1
    elif kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola:
        print("Şifreyi kontrol ediniz....")
        giriş_hakkı -=1
    elif kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola:
        print("Kullanıcı adı ve Parola hatalı")
        giriş_hakkı -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı.....")
        break
    if (giriş_hakkı==0):
        print("Giriş hakkınız bitti 5 dk sonra tekrar deneyiniz.....")
        break