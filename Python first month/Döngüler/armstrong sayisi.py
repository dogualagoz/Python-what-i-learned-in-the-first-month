# Kullanıcıdan bir sayı alınır ve dize olarak saklanır
sayi = input("Sayı:")

# Sayının basamak sayısını hesaplayarak "basamak_sayisi" değişkenine atanır
basamak_sayisi = len(sayi)

# Dize olan "sayi" bir tamsayıya dönüştürülür
sayi = int(sayi)

# Başlangıçta kullanılacak olan değişkenler tanımlanır
basamak = 0
toplam = 0
gecici_sayı = sayi

# "gecici_sayı" sıfırdan büyük olduğu sürece döngü devam eder
while gecici_sayı > 0:
    # "gecici_sayı"nın son basamağı "basamak" değişkenine atanır
    basamak = gecici_sayı % 10

    # "basamak" değeri "basamak_sayisi" üssü olarak "toplam" değişkenine eklenir
    toplam += basamak ** basamak_sayisi

    # "gecici_sayı"nın son basamağı çıkarılarak bir basamak sağa kaydırılır
    gecici_sayı //= 10

# Döngü sona erdikten sonra, "toplam" değeri "sayı"ya eşitse, sayı bir Armstrong sayısıdır
if toplam == sayi:
    print(sayi, "bir Armstrong sayısıdır.")
else:
    print(sayi, "bir Armstrong sayısı değildir.")
