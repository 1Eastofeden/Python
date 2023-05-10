
# x = str(3)
# y = int(2)
# o = float(1)
# print(type(x))
# print(type(y))
# print(type(o)) # type ile değişkenin türünü öğrenmek

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z) # x y z değişkenine sırayla "orange" "banana" "chery" değerlerini vermek

# # furis = ["banana", "watermelon", "apple"]
# # x = furis[2]
# # print(x) # list'enini içinden belirli bir elemanı seçmek

# x = "Python "
# y = "is"
# z = "awesome"
# print(x + y + z) # yazıları eklıyerek print'e yazdırmak

# x = "desta"
# def heydesta():
#     print(x + "love you")
# heydesta()  # function yazıları eklıyerek print'e yazdırmak

# x = 35e3
# y = 12E4
# z = -87.7e100
# desta = x + (y - z)
# print(desta) # float, 10'un kuvvetini belirtmek için "e" harfi bulunan bilimsel sayılar da olabilir

# x = 3+5j
# y = 5j
# z = -5j
# desta = x + (y - z)
# print(desta) # karmaşık sayılar sanal kısım olarak "j" ile yazılıri

# x = 45
# y = float(x)
# print(type(y)) # değişkenin içindeki verinin türünü değiştirmek

# import random 
# print(random.randrange(154,1500)) # rastgele modülü içe aktarın ve 154 ile 1500 arasında rastgele bir sayı görüntüleyin

# txt = "desta"
# if "desta" in txt:
#   print("ı love you desta") # yalnızca "desta" mevcutsa yazdırın

# txt = "The best things in life are free!"
# print("expensive" not in txt) # aşağıdaki metinde "pahalı" ifadesinin OLMADIĞINI kontrol edin

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.") # yalnızca "pahalı" mevcut DEĞİLSE yazdırın

# x = "desta"
# print(x[3:]) # 3'den başla almaya

# x = "desta"
# print(x[:3]) # 3'e kadar yaz

# x = "desta"
# print(x.upper()) # x değişkenindeki değeri büyük harfle yazar

# y = "DESTA"
# print(y.lower()) # x değişkenindeki değeri küçük harfle yazar

# x = "desta nurwati siamyah"
# print(x.strip()) # yöntem strip(), başlangıçtaki veya sondaki tüm boşlukları kaldırır

# a = " Hello, World! "
# print(a.strip()) # yöntem strip(), başlangıçtaki veya sondaki tüm boşlukları kaldırır

# a = "Hello, World!"
# print(a.replace("H", "J")) # yöntem replace(), bir dizeyi başka bir dizeyle değiştirir

# a = "Hello, World!"
# print(a.split(",")) # yöntem split(), ayırıcının örneklerini bulursa dizeyi alt dizelere böler

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c) # ralarına boşluk eklemek için şunu ekleyin "" a değişkeni değişkenle b değişkende birleştir ve c dedğişkenine'de topla

# age = 24
# txt = "My name is John, and I am {}"
# print(txt.format(age)) # format() dizelere sayı eklemek için yöntemi kullanın 

# x = "muhammed"
# print(x.capitalize()) # capitalize() ilk harfini büyük yapar

# txt = "muhammed çok yakışıklı muhammed götten siker muhammed am yalar muhammed meme sever"
# x = txt.count("muhammed")
# print(x) # count() belirtilen değer kaç kere döndü

# print(10 < 9) # false döner 
# print(10 > 9) # true döner

# x = 6
# y = 5
# o = x % y
# print(o) # mod almak

# x = 5
# y = 5
# o = x ** y
# print(o) # üstünü almak

# x = 5 
# y = 5 
# o = x // y
# print(o) # tam sayı ve ya değil 

# x = 4 + (4 * 9)
# print(x) # çarp sonra 4 ekle

# x = 7
# print(x < 10 and x > 4) # x küçüktür 10'dan ve x büyüktür 4'den

# x = 5
# print(x > 3 or x < 4) # x büyüktür 3'den ya da x 4 küçüktür x den

# x = 5 
# print(not(x > 3 and x < 10)) # not operatörü kullanark true dönmesi yerine false döndüreblirliz

# x = 5
# y = 4
# print(x is y) # değişkenlerinin aynı nesneyi mi gösterdiği kontrol edilir

# x = 6
# y = 4
# print(x is not y) # değişkenlerinin aynı nesneyi işaret etmedikleri kontrol edilir

# x = ["watermelon", "mushroms"]
# print("watermelon" not in x) # x de watermelon yok mu

# x = ["watermelon", "apple"]
# print("hello" not in x) # x de hello yok mu

# x = ["watermelon", "apple"]
# print("hello" in x) # hello varmı? x de

# x = ["watermelon", "apple"]
# print("watermelon" in x) watermelon varmı? x de

# x = 4
# y = 6
# if x | y: 
#     print(x, y) # x ya da y varsa print'e yaz

# x = 4
# y = 6
# if x & y:
#     print(x + y) # x ve y varsa x ve y'yi topla ve print'e yaz

# x = 100 + (5 * 5) - (742 * (1/12))
# print(x)

# list = ["watermelon", "cherry", "apple"]
# print(len(list)) # liste'nin kaç elamanı var ?

# list = ["watermelon", "cherry", "apple"]
# print(type(list)) # class list

# thislist = list(("apple", "watermelon"))
# print(type(thislist)) # list() i kullnarak list oluşturmak

# thislist = {"hello", "watermelon"}
# print(type(thislist)) # class set list türü

# thislist = {
#     "desta", "hello","muhammed"
# }
# print(type(thislist)) # class set list farklı yazım türü

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4]) # kiwi ye kadar olanları yaz

# list = ["hello", "desta"]
# list[0] = "muhammed"
# print(list) ## listenin 0 ıncı öğesine erişim değiştirmek

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist) # listenin sonuna bir öğe eklemek için append() yöntemini kullanın

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist) # belirli bir dizine bir liste öğesi eklemek için yöntemi kullanın insert() yöntem insert(), belirtilen dizine bir öğe ekler

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist) # geçerli listeye başka bir listeden öğeler eklemek için extend() yöntemi kullanın

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist) # liste nesnelerinin, sort() listeyi varsayılan olarak artan şekilde alfasayısal olarak sıralayacak bir yöntemi vardır

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist) # şu yöntemle bir listenin bir kopyasını oluşturun copy()

# thislist = ["hello", "çav", "ananısikerim"]
# print("ananısikerim" in thislist) # "ananısikerim" i bul thislist in içinden varsa true yoksa false döner

# thislist = {"hello"}
# thislist.add("orange")
# print(thislist) # list e yeni değeer eklemek add() ile

# thislist = {
#     "hello", "merhaba"
# }
# list = {
#     "yani", "bencede"
# }

# thislist.update(list)
# print(thislist) #list içersine list eklemek update() ile

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset) # listenini içersinden öğe çıkarmak remove() ile

# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset) # list'i tamamen silmek clear() ile

# thislist = {"feb", "jun", "may"}
# list = {"mon", "thu", "sun"}
# alllist = thislist.union(list)
# print(alllist) # 2 farklı listeyi union() ile birleştirmek

# thislist = {"feb", "jun", "may"}
# list = {"mon", "thu", "sun"}
# thislist.update(list)
# print(thislist) # 2 farklı listeyi update() ile birleştirmek

# x = int(4.9) 
# print(x) # floatsı kesiril sayıyı tam sayıya dönüştürmek

# a = 7.9 + 3
# print(a) # float sayı ve intesion sayı toplamak

# x = 1.1 + 1.1
# print(x) # float ve float objeyi toplamak

# print('hey \n nasılsın') # satır atlar

# print("hey \t malmısın") # boşluk yapar

# print("hey '\' naber") # "" kullanmak için kullanılır

# thislist = {"hello"}
# o = thislist.add("hii")
# print(thislist) # listeye ekleme add() ile

# fruits = {"apple", "banana", "cherry"}
# fruits.clear()
# print(fruits) #listeyi temizlemek clear() ile

# thislist = {"watermelon", "mushrooms"}
# x = thislist.copy()
# print(x) # listeyi kopyalamak copy() ile

# x = {"banana", "watermelon"}
# o = {"banana", "mushrooms"}
# y = o.difference(x)
# print(y) # iki liste arassındakı farklı elemanı bulup yazdırmak difference() ile

# thislist = {
#     "gender": "woman",
#     "name": "desta",
#     "age": "24"
# }
# o = thislist["age"]
# print(o) # listenini içinden age öğesinin karşılığını yazdırmak

# thislist = {
#      "gender": "woman",
#      "name": "desta",
#      "age": "24"
# }
# o = thislist.get("name") # get() ile birlikte karşılığını bulmak
# o = thislist.keys() # keys() ile birlikte anahtar kelimeleri değerleri değil anahtar kelimeleri alır yazar
# o = thislist.values() # value() ile birlikte anahtar kelimelerin değerlerini alır ve yazdırır
# o = thislist.items() # items() ile birlikte thislist'in keys() ve value() lerinin sınıflandırarak yazar
# print(o)

# thislist = {"gender": "man", "name": "muhammed", "age": "21"}
# newvalue = thislist["age"] = "55"
# print(thislist) # list'ye yeni değer atamak

# thislist = {"gender": "non-biray", "name": "non-name", "age": "non-age"}
# thislist.update({"name": "çağatay"})
# print(thislist) # update() kullanrak değeri değiştirmek

# thislist = {"gender": "non-biray", "name": "non-name", "age": "non-age"}
# thislist.pop("gender")
# print(thislist) # pop() kullanarak value() ve keys() i kaldırmak

# thislist = {"gender": "non-biray", "name": "non-name", "age": "non-age"}
# thislist.popitem()
# print(thislist) # popitem() ile son eklenen öğeyi kaldırmak

# thislist = {"gender": "non-biray", "name": "non-name", "age": "non-age"}
# del thislist["age"]
# print(thislist) #del kullanarak belirtilen value() ve keys() i kaldırmak

# thislist = {"gender": "non-biray", "name": "non-name", "age": "non-age"}
# for x in thislist:
#   print(x) # for döngüsünü kullanarak listedeki tüm keys() leri yazdırmak

# thislist = {"gender": "non-biray", "name": "non-name", "age": "non-age"}
# for x in thislist:
#   print(thislist[x]) # for döngüsü kullanarak listedeki tüm value() leri yazdırmak

# thislist = {"gender": "non-biray", "name": "non-name", "age": "non-age"}
# if thislist.get("gender"):
#     newgender = thislist["gender"] = "man"
#     newage = thislist["age"] = "21"
#     newname = thislist["name"] = "muhammed"
#     print(thislist)
# else: 
#     print("böyle bir değer yok") # thislist'in "gender" keys i varsa çalıştır

# x = input("lütfen sadece rakam giriniz")
# o = int(x)

# y = input("lütfen sadece rakam giriniz")
# p = int(y)

# up = o + p

# if up >= 100:
#     print("tebrikler işlem başarılı")
# else:
#     print("üzgünüz işlem başarısız") # sayıları toplayım 100 ve üsstündeyse if altındaysa else bloklarını çalıştırmak

# mat = input("matematik notunuz")
# intmat = int(mat) # matematik

# a = intmat / 2

# tur = input("türkçe notunuz")
# inttur = int(tur) # türkçe

# b = inttur / 2

# ing = input("ingilizce notunuz")
# inting = int(ing) # ingilizce

# c = inting /2

# fen = input("fen notunuz")
# intfen = int(fen) # fen bilimleri

# d = intfen / 2

# sos = input("sosyal bilgiler notunuz")
# intsos = int(sos) # sosyal bliglier

# e = intsos / 2

# din = input("din notunuz")
# intdin = int(din) # din

# f = intdin / 2

# x = a + b + c + d + e + f
# o = x / 3

# if o >= 85:
#     print("takdir belgesi aldınız", o)
# elif o >= 70:
#     print("teşşekür belgesi aldınız", o)
# elif o >= 50:
#     print("sınıfı geçtiniz", o)
# else:
#     print("sınıfta kaldınız", o)

# o = not True
# if o == False:
#     print("merhaba")
# else: 
#     print("hello") #not true değişenkini false olmasını sağlar

# x = 5
# while x < 1000000 :
#     x += 1 # x'i arttır
#     print(x)

# x = 4
# while x < 20 : 
#     x += 1
#     print(x)
#     if x == 17 :
#         break # döngüyü durdurur
#     else:
#         continue # döngüyü devam ettirir

# x = 66
# y = 44
# while x + y == 110 :
#     o = 99
#     p = 1 
#     while o + p == 100 :
#         print("ananı sikeyim")

# thislist = {"gender": "non-biray", "name": "non-name", "age": "non-age"}
# for x in thislist :
#   if thislist["age"] == "non-age" :
#    print("ananı sikerim")

# def hello() :
#     print("hello world")
# hello()

# thislist = {"gender": "non-biray", "name": "non-name", "age": "non-age"}
# def openlist():
#     global thislist  # thislist değişkenini global olarak tanımlayın
#     thislist.clear()
#     thislist = {"hello": "muhammed", "how are you today": "I'm good"}
#     print(thislist)
# openlist()

# def like(furits = "watermelon") : 
#     print(" I like a " + furits)
# like()

# def like(furits = "watermelon") : 
#     print(" I like a " + furits)
# like("apple")

# def like(x) : 
#     return 74 * x
# print(like(7)) #7 ile 74 ü çarp

# x = lambda a, b : a * b
# print(x(5, 6)) 

# class person : 
#     # thislist = ["gender", "name", "surname", "age", "tall"]
#     user = input("username")
#     gender = input("gender")
#     age = input("age")
#     thislist = []
#     thislist.append(user)
#     thislist.append(gender)
#     thislist.append(age)
#     print(thislist)
# person()

# class person :
#     def __init__(self, username, gender, age):
#         self.username = username
#         self.gender = gender
#         self.age = age
#         self.user_list = [username, gender, age]

# person1 = person("ahmet", "erkek", 25)
# person2 = person("ayşe", "kadın", 30)

# print(person1.user_list)
# print(person2.user_list)

# this = "watermelon"
# thisword = iter(this)

# print(next(thisword))
# print(next(thisword))
# print(next(thisword))
# print(next(thisword))
# print(next(thisword))
# print(next(thisword))
# print(next(thisword))
# print(next(thisword))
# print(next(thisword))
# print(next(thisword)) # 

# this = "watermelon"
# for x in this :
#     print(x)

# thislist = ["watermelon", "stawbery", "mushrom", "apple"]
# print(len(thislist[1])) # len ile karakter sayısına bakmak

# import module
# o = module.thislist["name"]
# print(o) # başka dosyadan bilgi almak

# import datetime
# x = datetime.datetime.now()
# print(x) # zamanı almak

# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%A")) # günü almak

# import datetime
# time = datetime.datetime.now()
# if time.month == 5 :
#     print("tebirkler")
# else :
#     print("üzgünüz")

# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%B")) # ayı almak

# x = min(5, 150)
# y = max(5, 150)
# print("min-x-:", x , "max-y-: ", y) # min() max() minimum ve maksimi değeri bulmak

# thislist = ["watermelon", "apple"]
# print(len(max(thislist))) # max() len() ile karakter sayısı en fazla olan elemanı buldum

# thislist = ["watermelon", "apple"]
# print(len(min(thislist))) # min() len() ile karakter sayısı en az olan elemanı buldum

# x = abs(-74.45)
# print(x) # pozitif değere döndürür abs()

# x = pow(4, 3)
# print(x) # 4 ün 3 üncü kuvveti = 64 pow()

# import math
# x = math.sqrt(40)
# print(x) # karekök bulmak

# import math
# x = math.ceil(4.4) # yukarıya yuvarlar
# y = math.floor(4.4) # aşşağıya yuvarlar
# print("x : ", x ,"y : ", y)

# import math
# x = math.pi
# print(x) # pi sayısının değeri

# import json
# x =  '{ "name" : "muhammed", "age" : "21", "country" : "turkey"}'
# y = json.loads(x)
# print(y) # json dosyasını python a çevirme loads()

# import json
# x = ["watermelon", "stawbery", "mushrom", "apple"]
# y = json.dumps(x)
# print(y) # python'dan json'a dönüştürmek dumps()

# import json
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None)) # nesneleri json'a dönüştürmek

# import re
# txt = "muhammed"
# write = re.search("^muh.*ammed$", txt)
# if write :
#     print("tebrikler", write)
# else : 
#     print("üzgünüz")

# import re
# thislist = "watermelon stawbery welcome"
# txt = re.findall("w", thislist)
# print(txt) # metindeki "w" aramak istediğin değeri arar findall()

# import re
# txt = "hello my name is muhammed"
# x = re.search("muhammed", txt)
# print(x) # değer arar search()

# import re
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x) # çümleyi böler split()

# import re
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x) # s leri 9 ile değiştirir sub()

# import re
# text = "She'is beatiful"
# one = re.findall("[a-z]", text)
# print(one) # küçük harfleri bulur [a-z]

# text = "muhammed"

# try : 
#    if text : 
#         print("tebrikler")
# except :
#     print("üzgünüz")

# text = input("isminizi yazınız: ")

# try :
#     if text == "muhammed" :
#         print("tebrikler!")
#     elif text != "muhammed" :
#         print("üzgünüz")     
# except:
#         print("üzgünüz")

