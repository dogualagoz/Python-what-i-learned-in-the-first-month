a = int(input("Sayı 1: "))
b = int(input("Sayı 2: "))

print("Değiştirilmeden önce değerler\na: {} b: {}\n".format(a,b))
a,b=b,a
print("Değiştirildikten Sonraki değerler \na: {} b: {}\n".format(a,b))


