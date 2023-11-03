toplam = 0
while True:
    sayi = input("Sayı:")
    if sayi == "q":
        break
    else:
        sayi = int(sayi)
        toplam+=sayi
print("Girdiğiniz Sayıların toplamı:",toplam)

