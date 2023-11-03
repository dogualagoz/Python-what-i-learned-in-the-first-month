"""
26 kuruş kilometrede 0.08 ml
100 km yol yapsın 80 ml yakıyor
26 tl yakıyo olsun

"""


print("Evden işe ne kadar benzine para harcıyorsun hesaplama")
x = float(input("Kilometrede kaç litre yakıyosun: "))
y = int(input("Kaç kilometre yol gittin: "))
z = float(input("litre başına kaç tl yakıyor"))
print("Tutar {} tl".format(x*y*z))

