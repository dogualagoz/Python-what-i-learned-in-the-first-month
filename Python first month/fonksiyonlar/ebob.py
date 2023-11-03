def ebob(sayi1,sayi2):
    i = 1
    ebob = 1
    while (i<=sayi1 and i<=sayi2):
        if (sayi1 % i == 0 and sayi2 % i == 0):
            ebob = i
        i+=1
    return ebob

sayi1 = int(input("Sayı-1: "))
sayi2 = int(input("Sayi-2: "))
print("Ebob:",ebob(sayi1,sayi2))