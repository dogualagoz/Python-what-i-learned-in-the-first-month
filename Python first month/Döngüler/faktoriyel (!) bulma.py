print("""
********************************
Faktoriyel Bulma Programı

Çıkmak için q'ya basın
********************************
""")

while True:
    sayi = input("Bir sayı giriniz: ")
    if sayi=="q":
        print("Program Sonlandırılıyor...")
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1):
            faktoriyel*=i
            print(faktoriyel)