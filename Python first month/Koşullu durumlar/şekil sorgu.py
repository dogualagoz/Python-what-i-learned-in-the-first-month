print("""
-----------------------------------
Şekil bulma programına hoşgeldiniz
-----------------------------------


""")
şekil= input("Hangi şekli öğrenmek istiyorsunuz ?")
print("Lütfen kenarları sırayla girin")
if (şekil== "Dörtgen"):
    print("Kenar uzunluklarını giriniz")
    a= int(input("Birinci kenar= "))
    b= int(input("İkinci kenar= "))
    c= int(input("Üçüncü kenar= "))
    d= int(input("Dördüncü kenar= "))
    if (a==b and a==c and a==d):
        print("Şekliniz kare")
    elif (a==c and b==d):
        print("Şekliniz dikdörtgen")
    else:
        print("Herhangi bir dörtgen")


elif (şekil== "Üçgen"):
    print("Kenar uzunluklarını giriniz")
    a = int(input("Birinci kenar="))
    b = int(input("İkinci kenar= "))
    c = int(input("Üçüncü kenar= "))
    if abs(a+b) >c and abs(a+c) > b and abs(b+c) > a:
        if (a==b and a==c):
            print("Şekliniz eşkenar üçgen")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("Şekliniz ikizkenar üçgen")
        else:
            print("Şekliniz çeşitkenar üçgen")


    else:
        print("Üçgen belirtmiyor")
else:
    print("Şekliniz üçgen veya dörtgen belirtmiyor")

