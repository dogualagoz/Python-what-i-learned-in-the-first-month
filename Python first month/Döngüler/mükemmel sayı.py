print("""
*************************************
Mükemmel sayı bulma programına hoşgeldiniz.

Mükemmel sayı nedir ?
Mükemmel sayı bölenlerini topladığında kendisine eşit olan sayılara denir.
(örn: 6 mükemmel sayıdır çünkü 1+2+3 = 6 olur)
programdan çıkmak için "q" ya basınız.
""")
while True:
    sayi = input("Sayı gir: ")
    i = 1
    toplam = 0

    if sayi== "q":
        print("Yine bekleriz...")
        break
    else:
        sayi = int(sayi)
        while(i<sayi):
            if (sayi % i == 0):
                toplam+=i
            i+=1
        if (toplam == sayi):
            print(sayi, "mükemmel bir sayıdır.")
        else:
          print(sayi, " mükemmel bir sayı değildir.")
