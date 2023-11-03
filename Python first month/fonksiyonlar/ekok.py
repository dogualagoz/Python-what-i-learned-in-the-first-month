def ekok_bulma(sayi1, sayi2):
    i = max(sayi1, sayi2)  # Daha büyük sayıdan başlayarak kontrol ederiz
    while True:
        if i % sayi1 == 0 and i % sayi2 == 0:
            ekok = i
            break  # Ekok bulunduğunda döngüden çıkılır
        i += 1
    return ekok

sayi1 = int(input("Sayı-1: "))
sayi2 = int(input("Sayı-2: "))
print("Ekok:", ekok_bulma(sayi1, sayi2))

