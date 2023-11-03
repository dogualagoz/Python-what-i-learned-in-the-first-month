"""
beden kitle indeksi: kilo/boy**

"""
print("Beden Kitle İndeksi Ölçere Hoş geldiniz")

kilo = int(input("Kilonuz (Kg cinsinden): "))
boy = float(input("Boyunuz (Metre Cinsinden): "))
bmi = kilo/(boy**2)
print("ölçülüyor...")


print("Beden kitle indeksiniz:", bmi)

