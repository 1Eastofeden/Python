
import random

thislist = ["blue", "green", "black", "brown", "yellow", "purple"]
random_color = random.choice(thislist)

print("İpucu: Rengin ilk harfi '{}'\n".format(random_color[0]))

user = input("Rengi tahmin edin: ")

if user == random_color:
    print("Tebrikler! Doğru tahmin ettiniz.")
else:
    print("Üzgünüz, yanlış tahmin ettiniz. Doğru renk: ", random_color)