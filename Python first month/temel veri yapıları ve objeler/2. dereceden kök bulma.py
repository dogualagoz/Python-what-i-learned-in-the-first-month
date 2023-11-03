
"""
2. Dereceden bir bilinmeyenli denklemin köklerini bulma
Denklem ax^2 + bx +c
Deltayı hesaplama: b**2 - 4*a*c
Birinci Kök: (-b-delta**0.5)/(2*a)
İkinci Kök: (-b+delta**0.5)/(2*a)
"""
print("Kök bulma programına hoşgeldiniz")
print("Sayıları giriniz")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b**2-4*a*c
x1 = (-b-delta**0.5)/(2*a)
x2 = (-b+delta**0.5)/(2*a)
print("Birinci kök: {}\n İkinci Kök: {}".format(x1,x2))