print("""**************************
Hesap Makinesi Programı

İşlemler:
      
1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
****************************
""")


a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))
işlem= input("İşlemi giriniz: ")
if işlem == "1":
    print("{} ile {} in toplamı {}'dir".format(a,b,a+b))
elif işlem== "2":
    print("{} ile {} 'in farkı {}'dir".format(a,b,a-b))
elif işlem== "3":
    print("{} ile {} 'in çarpımı {}'dir".format(a, b, a * b))
elif işlem== "4":
    print("{}'ın {} 'a bölümü {}'dir".format(a, b, a / b))
else:
    print("Geçersiz işlem......")



