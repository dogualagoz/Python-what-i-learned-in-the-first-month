print("""
*******************************
Kullanıcı Girişi
*******************************


""")
sys_kullanıcı_adı= "abcabc"
sys_parola= "1234"

kullanıcı_adı = input("Kullanıcı adı")
parola= input("Parola:")

if (kullanıcı_adı==sys_kullanıcı_adı and sys_parola != parola ):
    print("Parola hatalı...")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola== sys_parola):
    print("Kullanıcı adı hatalı...")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("Kullanıcı adı ve Şifre hatalı.....")
else:
    print("Sisteme başarıyla giriş yapıldı.....")