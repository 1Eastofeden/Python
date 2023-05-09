
import time

# Geri sayım süresini belirleyin
times = int(input("Geri sayımı başlatmak için rakam giriniz: "))

# Fonksiyonumuz her saniye çağrılacak ve zamanı ekrana yazdıracak
def my_func():
    print(time.time())

# Geri sayım yapmak için while döngüsü kullanın
while times > 0:
    my_func()
    time.sleep(1)
    times -= 1
    print(times)  # Kalan süreyi ekrana yazdırın

# Geri sayım tamamlandığında mesaj gösterin
print("Geri sayım tamamlandı!")
