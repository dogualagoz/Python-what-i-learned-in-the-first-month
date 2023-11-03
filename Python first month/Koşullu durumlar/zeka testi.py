print("Zeka Testine Hoşgeldiniz. Gelen sorulara 1 ila 3 arasında puan verin")
print("1 = Katılmıyorum")
print("2 = Kararsızım")
print("3 = Katılıyorum")
a= int(input("1) Kuran kursları cemaatler tarikatlar falan kapatılmalı"))
if a>=4:
      print("Yanlış sayı girdiniz")
elif a<1:
      print("Yanlış sayı girdiniz")
b= int(input("2) Atatürk'ü sevmiyorum demek ifade özgürlüğü değildir"))
if b>=4:
      print("Yanlış sayı girdiniz")
elif b<1:
      print("Yanlış sayı girdiniz")
c= int(input("3) Arapça kutsal dil değildir ezanin türkçe olmasında sıkıntı yok"))
if c>=4:
      print("Yanlış sayı girdiniz")
elif c<1:
      print("Yanlış sayı girdiniz")
if a+b+c==9:
      print("ASLAN ATATÜRKÇÜ KARDESİM BENİM")
elif 7<a+b+c<9:
      print("Normal zeka seviyen var")
elif 3<a+b+c<=7:
      print("Dostum psikolojik tedavi görmeye başlayabilirsin")
elif a+b+c<=3:
      print("ŞERİATÇİ P#!*?")
