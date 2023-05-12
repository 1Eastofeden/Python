import random
import time

# Kelime listesi
liste = ["elma","armut","karpuz","incir","kestane","ceviz","fındık","fıstık","kaju","muz","hindistancevizi","hurma","kayısı","şeftali","greyfut","portakal","mandalin","limon","nektari"]

# Doğru kelime sayısı
dogru_sayisi = 0

# Toplam cümle sayısı
cumle_sayisi = 0

# Sayaç
saniye = 60

while saniye > 0:
    # Rastgele kelime seçme
    kelime = random.choice(liste)
    print(f"Saniye: {saniye}")
    print(f"Kelime: {kelime}")
    
    # Başlangıç zamanı
    baslangic_zamani = time.time()
    
    # Kullanıcıdan cevap alma
    cevap = input("Metni yazınız: ")
    
    # Bitiş zamanı
    bitis_zamani = time.time()
    
    # Geçen süre
    gecen_sure = bitis_zamani - baslangic_zamani
    
    # Doğru cevap kontrolü
    if cevap.lower() == kelime.lower():
        print("Tebrikler, doğru cevap!")
        dogru_sayisi += 1
    else:
        print("Maalesef yanlış cevap.")
    
    cumle_sayisi += 1
    
    # Sayaç azaltma
    saniye -= int(gecen_sure)
    
print("Süre doldu!")
print(f"Doğru kelime sayısı: {dogru_sayisi}")
print(f"Toplam cümle sayısı: {cumle_sayisi}")
print(f"Yanlış kelime sayısı: {cumle_sayisi - dogru_sayisi}")
