birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]


def okunus(sayi):
    birinci = sayi %10
    ikinci = sayi //10

    return onlar[ikinci] + " " + birler[birinci]

while True:

    sayi = int(input("Sayi giriniz:"))
    print(okunus(sayi))