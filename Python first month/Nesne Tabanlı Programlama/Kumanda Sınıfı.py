import random
import time


class Kumanda():
    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["TRT"], kanal="TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyon Zaten Açık....")
        else:
            print("Televizyon Açılıyor....")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon Zaten Kapalı....")
        else:
            print("Televizyon Kapatılıyor....")
            self.tv_durum = "Kapalı"

    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Arttır: '>'\nÇıkış: çıkış")

            if cevap == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif cevap == ">":
                if self.tv_ses != 100:
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            elif cevap == "çıkış":
                print("Ses Güncellendi:", self.tv_ses)
                break
            else:
                print("Geçersiz bir komut girdiniz. Lütfen tekrar deneyin.")

    def kanal_ekle(self, kanal_ismi):
        print("Kanal Ekleniyor....")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi.....")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum, self.tv_ses,
                                                                                          self.kanal_listesi,
                                                                                          self.kanal)


kumanda = Kumanda()
print("""
    Televizyon Uygulaması

    1. Tv Aç
    2. Tv Kapat
    3. Ses Ayarları
    4. Kanal Ekle
    5. Kanal Sayısını Öğrenme
    6. Rastgele Kanala Geçme
    7. Televizyon Bilgileri

    Çıkmak için "q" ya basın.
""")

while True:
    islem = input("İşlemi Seçiniz: ")

    if islem == "q":
        print("Program Sonlandırılıyor...")
        break
    elif islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapat()
    elif islem == "3":
        kumanda.ses_ayarlari()
    elif islem == "4":
        kanal_isimleri = input("Kanal isimlerini virgül ile ayırarak girin: ")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif islem == "5":
        print("Kanal Sayısı:", len(kumanda))
    elif islem == "6":
        kumanda.rastgele_kanal()
    elif islem == "7":
        print(kumanda)
    else:
        print("Geçersiz İşlem......")








