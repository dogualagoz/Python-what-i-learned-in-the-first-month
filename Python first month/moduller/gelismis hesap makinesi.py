import math
print("""
**************************************
Hesap makinesine Hoşgeldiniz
İşlem Seçiniz: 


1. Toplama             11. Ebob

2. Çıkarma             12. Ekok

3. Çarpma              13. Logaritma 

4. Bölme               

5. Kuvvetini alma

6. Tam bölme

7. Kalan bulma

8.Mutlak Değer

9.Faktoriyel

10.Karekök

************************************


""")

işlem = int(input("İşlem seçiniz: "))

while True:
    if (işlem== 8 or 9 or 10):
        a = float(input("Sayı giriniz: "))
        if işlem == 8:
            print("Sayının mutlak değeri:",math.fabs(a))

        elif işlem == 9:
            print("Sayının faktoriyeli:",math.factorial(a))

        elif işlem == 10:
            print("Sayinizin karekökü",math.sqrt(a))
    else:
        a = float(input("Sayı 1: "))
        b= float(input("Sayı 2: "))
        if işlem == 1:
            print("{} ile {} toplamı {}'dir".format(a,b,a+b))









