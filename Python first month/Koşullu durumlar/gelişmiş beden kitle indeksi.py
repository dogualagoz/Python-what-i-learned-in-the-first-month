print("Beden kitle indeksi ölçere hoşgeldiniz......")
a= int(input("Kilonuz: "))
b= float(input("Boyunuz: "))
bmi= a/(b**2)
if bmi<18.5:
    print("Zayıfsınız kilo almanız gerekli.")
elif 18.5<=bmi<25:
    print("Kilonuz normal düzeyde.")
elif 25<=bmi<30:
    print("Fazla kilonuz var verseniz iyi olur.")
else:
    print("Obezsin kilo ver abicim.")