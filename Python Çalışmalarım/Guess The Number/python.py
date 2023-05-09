
import random

thislist = ["1","2","3","4","5","6","7","8","9"]
randoms = random.choice(thislist)

while True:
    user = input("Sayıyı tahmin et (1-10) ! ")

    if user == randoms :
        print("Tebrikler, doğru tahmin ettiniz!")
        break
    else :
        print("Üzgünüz, yanlış tahmin ettiniz. Tekrar deneyin.")