# Yorum satırı

# tekli yorum satırı

"""
Çoklu Yorum satırı
'''
" '' "
'''
"""

# ekrana yazdırma
# print("Python süper bir dil")
# print('buraya da yazılır')
# print("""piton diğer dillere göre,
# daha pratiktir""")

# print("Berkay","Ülger")
# print("Berkay"+"     "+" Ülger")


# print("bugün {1} giderken {0} düştü".format("1 kişi","okula"))

# dil = "python"
# print("{} dilini çok seviyorum".format(dil))
# print("{d} dilini çok seviyorum".format(d="python"))

# benim adım berkay soyadım ülger okula gidiyorum.
# yukardaki cümlede ad ve soyad sonradan yazılıcak okula kısmı için alan oluşturulcak

# print("benim adım {0} soyadım {1} {2} gidiyorum.".format("Berkay", "Ülger", "yazlığa"))

# print("18 çarpı 17 eşittir {}".format(carpim))
# print("18 çarpı 17 eşittir " + str(carpim))

# == 2 sayısal degişken olsun bunları çarpıp "çarpım sonucu:.. "

# s1 = 10
# s2 = 20
# text = "çarpımın sonucu = {}".format(s1*s2)
# print(text.format(s1*s2))
# print(text)

# değişkenlerde hangi semboller kullanılmaz
# 3deger
# -deger
# /deger
# deger/
# deger)

# deger3 =
# deg1er=
# deger_ =
# deg_er =

# değişkenlerde atama işlemi nasıl yapılır

# s1 = 10
# s1 = s1 + 5
# print(s1)


# değişkenlerde operatör işlemleri
# + toplama
# - çıkarma
# * çarpma
# / bölme
# % mod alma
# ** kare alma
# // tam bölme
# = atama

# print(10+20)
# print(10-20)
# print(10*20)
# print(10/20)
# print(20%10)
# print(20**10)
# print(20//3)


# değişkenlerde çoklu atama

# s1,s2,s3,s4 10 sayısını gönder
# s1=s2=s3=s4=10

# değişken değiştirme

# s1 = 10
# s2 = 20
# s3 = 30
# s1=30, s2=10, s3=20
# s1,s2,s3 = s3,s1,s2
# print(s1,s2,s3)

# x içine y, yiçine z, z içine x gönderilcek
# x=5
# y=15
# z=25
# print(x,y,z) 15,25,5
# x,y,z = y,z,x
# print(x, y, z)


# değişkenlerde type() çeşitleri
# type=integer kısaltma=int tr=tam sayılar
# x=10
# type=float kısaltma=float tr=virgüllü sayılar
# x=10.2
# type=string kısaltma=str tr=metin
# x="10 metin"
# type=boolean kısaltma=bool tr=doğru yanlış
# x=True
# type=liste kısaltma=list tr=liste
# x = [1,2,"üç","dört"]
# type=tuple kısaltma=tuple tr=değiştirilmez liste
# x = (1,2,"üç","dört")
# x = 1,2,"üç","dört"
# type=set kısaltma=set tr=küme
# x = {1,2,"üç","dört"}
# type=dictionary kısaltma=dict tr=sözlük
# x = {"key1": "value1", "key2": "value2"}

# x=None nonetype


# print("""

# VERİ TÜRLERİ
# """)

# deger = "Merhaba Dünya"
# print("1)" , type(deger) )
# deger = 12
# print("2)" , type(deger) )
# deger = [1,2,"üç"]
# print("3)" , type(deger) )
# deger = (1,2,"üç")
# print("4)" , type(deger) )
# deger = {"key1": "value1", "key2": "value2"}
# print("5)" , type(deger) )
# deger = {"eleman1", "eleman2"}
# print("6)" , type(deger) )
# deger = True # yada False
# print("7)" , type(deger) )
# deger = None
# print("8)" , type(deger) )


# // type değiştirme
# text = "22"
# s1 = 10
# toplam = s1 + int(text)

# toplam = str(s1) + text

# t1 = "10.7"
# t2 = "12"
# t3 = 7
# toplam = int(float(t1)) + int(t2) + t3
# print(toplam)

# a içinde 25 değeri olsun x içinde de "10"
# 35, 2510
# a=25
# x="10"
# print( a + int(x) )
# print( str(a) + x )

# x içinde "55" olsun y içinde "35" z içinde 20
# 5555, 3575, 110
# x = "55"
# y = "35"
# z=20
# print( x + str(int(y)+z) )
# print( y + str(int(x) + z) )
# print( int(x)+ int(y) + z )

# s1 = 12, s2 = 56, s3 = "34", s4 = "18"
# 3090 6852 10218
# s1,s2,s3,s4 = 12,56,"34","18"
# print( str(s1 + int(s4)) + str(s2 + int(s3)) )
# print( str(s1+s2) + str( int(s3) + int(s4) ) )
# print( str(s1+s2+ int(s3)) + s4 )


#
# s1 = 24, s2 = 44, s3 = "14", s4 = "55"
# 8255, 6968, 11324
# s1,s2,s3,s4 = 24,44,"14","55"

# print( str(s1 + s2 + int(s3)) + s4 )
# print( str(int(s3) + int(s4)) + str(s1+s2) )
# print( str(s2+int(s3)+int(s4)) + str(s1) )

# ÖDEV
# s1=8.7, s2=2, s3="10.8", s4="20"
# 40, 81022, 3010.8, 2219.5, 1228.7

# s1,s2,s3,s4 = 8.7,2,"10.8","20"

# print( int(s1) + s2 + int(float(s3)) + int(s4) )
# print( str(int(s1)) + str(int(float(s3))) + str(s2+int(s4)) )
# print( str(int(s1)+s2+int(s4)) + (s3) )
# print( str(s2+int(s4)) + str(s1+float(s3)) )
# print( str( s2 + int(float(s3))) + str(s1 + int(s4)) )

# ÖDEV
# t1=23, t2=22, t3="5", t4="12.2"
# 45512, 12.250, 557.2,
# t1,t2,t3,t4 = 23,22,"5","12.2"
# print( str(t1+t2) + (t3) + str(int(float(t4))) )
# print( (t4) + str(t1+t2+int(t3)) )
# print( (t3) + str(t1+t2+float(t4)) )

# len() uzunluk komutu

# text = "merhaba length"
# print(len(text))
# list1 = [1,2,"üç","elma"]
# print( len(list1) )
# dict1 = {"elma","armut","kiraz"}
# print( len(dict1) )
# sayi1 = 4,2
# print( len(sayi1) )

# input dışardan girdi

# fname = input("Adını Buraya Gir: ")
# sname = input("Soyadınızı Buraya Giriniz: ")
# print(fname,sname)

# dtarih = input("doğum tarihini giriniz: ")
# yas = 2023 - int(dtarih)
# print(yas)

# === alıştırma dışardan girilen ad soyad ve doğum tarihini print ile ekrana yazdır


# s1=10, s2=20 dışardan alınıcak, sayıları önce topla sonra birleştir, sonuc = 301020
# s1= input("1.sayı: ")
# s2= input("2.sayı: ")

# sonuc = str(int(s1)+int(s2)) + (s1+s2)
# print(sonuc)

# ***  kullanıcıdan girilen 25, 30, 45 sayılarıyla 7030, 2575, 10025 olarak yazdır

# s1= input("s1: ")
# s2= input("s2: ")
# s3= input("s3: ")

# print( str(int(s1)+int(s3)) + s2 )
# print( s1 + str(int(s2) + int(s3)) )
# print( str(int(s1) + int(s2) + int(s3)) + s1 )


# === alıştırma x = 4.4 y="6" z = "5.2" toplama işlemi kullanılarak 15 sayısı bulunacak int() str() float()
# x = 4.4
# y = "6"
# z = "5.2"
# print( int(x) + int(y) + int(float(z)) )

# dışardan girilen sayıların ortalaması

# s1 = int(input("s1: "))
# s2 = int(input("s2: "))
# ortalama = (s1+s2)/2
# print(ortalama)

# === alıştırma 4 sınavın ortalaması alınacak

# s1 = int(input("s1: "))
# s2 = int(input("s2: "))
# s3 = int(input("s3: "))
# s4 = int(input("s4: "))
# ortalama = (s1+s2+s3+s4)/4
# print(ortalama)

# === alıştırma vizenin %40 finalin %60 alınarak öğrencinin geçip geçmediğini hesapla

# vize = int(input("vize: "))
# final = int(input("final: "))
# note = int(vize*.4 + final*.6)
# print(note)

# === alıştırma dışardan 3 tane değer girilecek bu değerlerin sırasıyla yüzde %20 %40 %70 sonra çarpılacak ekrana yazdır

# print( int(input("s1: "))*.2*.4*.7 * int(input("s2: ")) * int(input("s3: ")) )

# /// string parçalama
# text[ başlangıç : bitiş : artış ]
# text = "Merhaba String Parçalama"
# print( text[2] ) # r
# print(text[2:])  # rhaba String Parçalama
# print(text[2:7])  # rhaba
# print(text[2:16:2])  # raaSrn
# print(text[:5])  # Merha
# print(text[-4:])  # lama
# print(text[-16:-10])  # String
# print(text[-16:14])  # String

# === alıştırma sadece adınızı ve soyadınızı yazdırın "benim adım berkay soyadım ülger"
# ekrana çıktısı = berkay ülger
# text = "benim adım berkay soyadım ülger"
# print( text[11:17] , text[-5:] )

# print("merhaba python"[:4])

# === alıştırma text="4 sayısı 4'e eşittir ve 8 2nin kübüdür." bu cümleyi "ve" yazan yerden ikiye ayır
# text = "4 sayısı 4'e eşittir ve 8 2nin kübüdür."
# print(text[:21])
# print(text[24:])

# === alıştırma text = "bugün neos akademi etkinliği varmış"  akademi'den sonrasını ekrana yazdır.
# text = "bugün neos akademi etkinliği varmış"
# print(text[19:])

# === alıştırma text = "arabamın markası kia modeli rio ve 2016 modeldir" marka: model: ve yıl: yazdır.
# text = "arabamın markası kia modeli rio ve 2016 modeldir"
# print("marka:" + text[17:21],"modeli:"+text[28:31], "yıl:"+text[35:39] )

# === alıştırma text = "hava güzel gibiydi ama değilmiş" güzel yerine kötü yazdırın 
# çıktı = "hava kötü gibiydi ama değilmiş"
# text = "hava güzel gibiydi ama değilmiş"
# print( text[:5]+"kötü"+text[10:] )

# == text = "markete gittim bir elma 2 armut aldım." ekrana =  "gittim markete bir armut bir elma aldım"
# text = "markete gittim bir elma 2 armut aldım."
# print( text[8:15] + text[:8] + text[15:19] + text[-12:-6] + text[15:24] + text[-6:] )

# == text = "sonucunu düşünen kahraman olamaz" ekrana = "düşünen kahraman sonuncu olamaz"
# text = "sonucunu düşünen kahraman olamaz"
# print( text[9:26] + text[:4]+text[2]+text[4:6] + text[-7:]  )

# ÖDEV ==== text="ben de kestane yerim" sadece text değişkeni kullanılarak çıktı="bir tane erik yedim" 

# ÖDEV ==== text="sardılar dört bir yanımı, benim" çıktı="sardı beni bir yalan"

# == ÖDEV = "bir gün batıcak şehirdeki tüm güneşler" çıktı = "tüm gün şehirde batıcak güneşim"

# # /// string metotları ======================
# # upper, lower, title, capitalize, index, find, count, strip, split, replace 

# text = "Merhaba String Methodu..,, 5"

# # BÜYÜK KÜÇÜK HARF METHODLARI
# print(text.upper())  # MERHABA STRING METHODU
# print(text.lower())  # merhaba string methodu
# print(text.title())  # Merhaba String Methodu
# print(text.capitalize())  # Merhaba string methodu

# # İNDEX METHODLARI
# print(text.index("Str"))  # 8
# print(text.find("Str"))  # 8
# print(text.find("str"))  # -1

# # TEKRARLARI BULMA
# print(text.count("e")) # 2
# print(text.count("Me")) # 2

# # SAĞ VE SOLDAN ÇIKARILCAKLAR
# print(text.strip(".,5 "))

# # LİSTEYE DÖNÜŞTÜRME
# print( text.split(" ") )

# # TEXT İÇERİĞİ DEĞİŞTİRME replace(old, new, adet)
# print(text.replace("t","d",3))
# print(text.replace("Merhaba ","")) # Çıkartma yapmak istediğimiz
# print(text.replace("Merhaba","Merhaba güzelim seni üzerim")) # Ekleme yapmak istediğimizde


# # === ÖDEV tesxt = "buradaki mağralardan yarasa geliyor" yarasa yazısını upper kullanarak büyüt
# text = "buradaki mağralardan yarasa geliyor"
# print( text[:20] + text[20:27].upper() + text[27:] )

# # === ÖDEV "benim adım ... soyadım ..." ad ve soyadı dışarda tanımlayın printe ad ve soyadı yazdırın 
# # len(), find()

# ad= "Berkay"
# soyad = "Ülger"
# text = "benim adım ... soyadım ..."
# print( text[:text.find("...")] + ad + text[-12:-3] + soyad )

# === ÖDEV "4 sayısı 8'e eşittir ve 4 2nin kübüdür." bu cümleyi düzeltin
# text = "4 sayısı 8'e eşittir ve 4 2nin kübüdür."
# print( text.replace("4", "8").replace("küb", "küp") )


# === alıştırma username=".,.? ..!!berkayulger..*" kullanıcı adını ekrana yazdır
# username = ".,.? ..!!berkayulger..*r"
# username = username[:-1].strip(".,? *!")  # berkayulger
# print( username )

# === alıştırma  " *   BUGÜN HAVA Güzel  .., " yazı küçülecek, boşluklar ve işaretler gidicek
# text = " *   BUGÜN HAVA Güzel  .., "
# text = text.lower().strip(" *.,")
# print(text)
# print("\033[96mMerhaba")

# === alıştırma text = "benim para sayan pahalı bilgisayarım" listeye dönüştür sonra pahalı kelimesini yazdır
# text = "benim para sayan pahalı bilgisayarım"
# text = text.split()
# print(text[3])

# === alıştırma text = "benim para sayan pahalı bilgisayarım" baş harfleri büyüt ve pahalı kelimesini çıkar
# text = "benim para sayan pahalı bilgisayarım"
# text = text.title()
# text = text.replace("Pahalı ", "")
# print(text)

# "tutmayın küçük enişteyi bırakın gitsin."
# "tutma enişteyi bırakın gitsin."
# text = "tutmayın küçük enişteyi bırakın gitsin."
# text = text[:5] + " " + text[text.find("enişte"):]
# print(text)


# // TUPLE
# tuple1 = (1,2,3,"dört","beş")
# tuple1 = 1,2,3,"dört","beş",2,2

# print( tuple1.count(2) )
# print( tuple1.count(3) )
# print( tuple1.index("beş") )

# tuple1 = list(tuple1)
# print(tuple(tuple1))
# tuple1[3] = "asdasd"
# print(tuple1[3])

# LİSTE
# val1 = 10
# list1 = [1,2,1.2,"elma","merhaba",["a","b"],{0:"v1"},val1]
# print(list1[6][0])

# /// liste parçalama ve eleman çağırma
# list1[ başlangıç : bitiş : artış ]
# list1 = [11,22,"elma","armut","a","b",33]
# print(list1[2]) # elma
# print(list1[2:])  # ['elma', 'armut', 'a', 'b', 33]
# print(list1[2:4])  # ['elma', 'armut']
# print(list1[1:6:2])  # [22, 'armut', 'b']
# print(list1[::3])  # [11, 'armut', 33]
# print(list1[:-3:1])  # [11, 22, 'elma', 'armut']


# // iç içe listeler

# alıştırma list4 = [1, 2 , 3, 4, 5, [6, 7 , [10, "list4", 12 ]] ]   12 sayısını getirin
# list4 = [1, 2, 3, 4, 5, [6, 7, [10, "list4", 12]]]
# print(list4[-1][-1][-1])

# # alıştırma list1 = [1,2,3,4,[11,{1:"bir","10":"on"}]]  "on" yazanı getir
# list1 = [1, 2, 3, 4, [11, {1: "bir", "10": "on"}]]
# print(list1[-1][-1]["10"])

# === Alıştırma
# list2 = ["bir","iki", [ "elma","armut","kiraz" ]]
# list1 = ["red","blue","orange",list2,"black"]
# listzero = [1,2,list1,3,4,5]
# print(listzero[2][-2][-1][1])
# yukarıdaki listeler içerisinden listzero kullanılarak "armut" ekrana yazdırın




# /// 2 listeyi toplama ve eşitlik kurma
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,0]
# list1 = list1+list2
# list1 += list2
# list1 += list2[-2:]
# list1 += [list2[-2]]
# print(list1)

# list1 = [1,2,3,4]
# list1[2] = "elma" # liste içindeki eleman değiştirme
# print(list1)

# eşitlik kurma
# list1 = [1,2,3,4] 
# list2 = list1
# list2 += [5]
# print(list2)

# eşitlikten kurmadan kopyalamak
list1 = [1,2,3,4] 
# list2 = []
# list2 += list1
# list2[0] = "elma"
# print(list2)

# list2 = list1.copy()

# /// liste metotları


# EKLEME methodları
# list1 = [1,2]

# list1 += [3] # manuel
# list1.append(4) # tek bir eleman ekler 
# list1.insert(3,"elma") # insert(index, eklenen)
# list1.extend([3,4,5]) # extend(listeyi üzerine ekler)

# print(list1)

# ÇIKARMA methodları
# list1 = [1,2,3,5,"muz",4]
# list1.pop(2) # pop(index) içi boş ise son elemanı çıkartır
# list1.remove("muz") # remove(eleman) yazılan elemanı çıkartır
# del list1[2] # indexe göre siliyor
# list1.clear() # boş liste
# print(list1)

# Listeyi ter çevirme 

# list1 = [10,2,33,8,5,2]
# list1.reverse()
# list1 = list1[::-1]
# # Listeyi sıralama
# list1.sort()
# list1.reverse()
# # tekrarları bul
# print(list1.count(2))
# # index bul
# print(list1.index(33))
# print(list1)


# ===============================================================
# *** ödev "benim para sayan pahalı bilgisayarım"
# 1) para yazısını içinden çıkart ekrana yazdır
# 2)"PARA" haline getir harflerini büyütecek ve ekrana yazdır
# 3)geri yerine yerleştirilecek ekrana yazdır

# text = "benim para sayan pahalı bilgisayarım"
# chars = "sayan"
# paraBa = text.find(chars) # paranın başlangıç indexini verir
# paraBi = text.find(chars) + len(chars) # paranın bitiş indexini verir
# para = text[paraBa:paraBi] # paranın cümle içerisinde konumunu kendisi bulur.

# text = text.replace(chars, "")  # "benim  sayan pahalı bilgisayarım"
# para = para.upper()
# para = para[::-1]

# text = text[:paraBa] + para + text[paraBa:]
# # benim PARA sayan pahalı bilgisayarım
# print(text)


# ÖDEV === liste1 içinde elma audi armut ford kivi kia çilek olsun
# bunlardan sadece araba olanları list2, meyve olanları list3e sırala
# text = "elma audi armut ford kivi kia çilek"
# list1 = text.split()
# list2 = list1[::2] # indexi çift olanları alır
# list3 = list1[1::2] # indexi tek olanları alır
# print(list2)
# print(list3)

# ÖDEV === ev araştırma ödevi 33 sayısının eski indexini nasıl buluruz?

# list2 = [22,11,44,111,333,2323,64,23,33]
# list1 = list2.copy()
# list2.sort()
# print(list2)
# print(list2.index(33))

# # ÖDEV === 111 saysını indexe göre çekicek bu sayıyı 2 ile çarpıp geri listeye yerleştircek
# list2[3] = list2[3] * 2
# print(list2)
# ÖDEV === boş list1 içerisine 4 meyve tanımla ve 3. indextekini patates ile değiştir
# list1 = []
# list1 += ["elma", "armut", "kiraz", "karpuz"]
# # list1[3] = "patates"
# list1.insert(3,"patates")
# list1.pop()

# # ÖDEV === list2 3 yazılım dili girilsin sonuna "python" ekle ve 2.indexteki listeden çıkar
# list2 = ["javascript", "java", "dart"]
# list2.append("python")
# list2.pop(2)
# print(list2)



# === list1 içine 4 meyve gir 3.meyveyi 4 ile yerdeğiştir. ilk indexe "muz" gir toplamda 5 eleman olucak
# list1 = ["elma","karpuz","kavun","kiraz"]
# list1[2],list1[3] = list1[3],list1[2]
# list1.insert(0,"muz")
# print(list1)
# # # # === list1 tersten yazdır ve ilk elemanı listeden çıkar daha sonrada listeyi büyükten küçüğe sırala
# list1.reverse()
# list1.pop(0)
# list1.sort()
# list1.reverse()
# print(list1)

# === list1 = [1, 55, 7, 12,5,11, 200] sort ile büyükten küçüğe sırala ve 12 sayısını ekrana yazdır. index kullanılacak
# list1 = [1, 55, 7, 12, 33, 11, 88, 200]
# list1.sort()
# list1.reverse()
# print(list1)
# print("index numarası:",list1.index(12),"- bu indexe gelen sayı",list1[list1.index(12)])


# === list2 = ["elma","armut","kiraz","patates"] içinden 0 2 indexin yazılarını büyüt ve liste2nin 1 ve 3 indexi yer değiştir
# list2 = ["elma", "armut", "kiraz", "patates"]
# list2[0] = list2[0].upper()
# list2[2] = list2[2].upper()
# list2[1],list2[3] = list2[3],list2[1]
# print(list2)

# === tek inputtan girilen 4 meyveleri listeye dönüştür,
# 2.indexteki yazıları büyüt ve her harfi birer liste elemanı olarak tekrar ekle
# text = input("4 meyve gir: ")
# text = text.split()

# # text.extend(text[2])
# text += text[2].upper()
# print(text)
# print(list(text[2])) # listeye dönüştürme

# /// if elif else ,karşılaştırma operatörleri
# Karşılaştırma operatörü
# == eşit mi
# != eşit değil mi
# < küçük mü
# > büyük mü
# <= küçük eşit mi
# >= büyük eşit mi
# and or
# in is not

# if True:
#    print("çalışır mı?")
   
# if False!=True:
#    print("çalışır mı?")

# print(False != True)
# if True == 1:
#    print("çalışır mı?")

# print(True>False)
# print(False != 0)
# print(1 != False)
# print(5%2 == 1)

# text = 2323

# if(){
# kasdjhasgd  
#          ahsgdjasgdj
# }

# if text:
#    print("if çalıştı")
#    if "asd":
#       print("asd")
# elif 18 >= 19:
#    print("elif çalıştı")
# else:
#    print("else çalıştı")
   

# === öğrencinin ortalaması 50 üstüyse geçti altıysa kaldı yazdırsın
# if int(input("öğrenci notu: ")) >= 50:
#    print("geçti")
# else:
#    print("kaldı")
   





# === partiye girenlerin yaşı 18 in üstündeyse ekrana girebilir altıysa giremez yazdırsın. 55 yaş üstü giremez yazsın
# yas = int(input("yaşınız kaç: "))

# if 55>yas>18:
#    print("girebilir")   
# else:
#    print("giremez")   
   
# if yas > 18 and yas < 55:
#    print("girebilir")   
# else:
#    print("giremez")   
# === kullanıcıdan girilen isim soyisim baş harfleri büyükse ekrana kaydı tamamla yazsın
# ad = input("ad ve soyadı yazınız: ")
# if ad.istitle():
#    print("kaydınız tamamlandı")
# else:
#    print("Baş harfleri büyük giriniz...")

# === kullanıcıdan girilen 2 veri alıyruz eğer sayılardan oluşuyorsa ikisini
# toplasın değilse ekrana "yalnızca sayı girilsin"
# s1 = input("s1: ")
# s2 = input("s2: ")
# if s1.isnumeric() and s2.isnumeric():
#    print(int(s1)+int(s2))
# else:
#    print("yalnızca sayı giriniz")



# === alıştırma text = "hakkında/?q="+ input("kategori girilsin: ")
# tarayıcıdaki teknoloji yazısını çekiniz teknoloji kısmı inputtan girilecek
# eğer oyun katagorisiyse yazı büyüsün ekrana yazsın eğer teknolojiyse ekrana telefon modeli yazdırsın
# text = "anasayfa/?q=" + input("kategori girilsin: ")

# search = text[text.find("?q=")+3:]

# if search == "teknoloji":
#    print("televizyon almak istemisin! ")
# elif search == "oyun":
#    print("oyunlarda yüzde 40 indirim! ")
   

# === ÖDEV girilen sayı pozitif mi negatifmi
# s1 = int(input("s1: "))
# if s1 < 0:
#    print("negatif")
# elif s1 > 0:
#    print("pozitif")
# else:
#    print("nötr")

# ===== ÖDEV =====
# vize ve final iki not inputtan alınır
# vizenin ortalaması %40 finalin ortalaması %60tır.
# iki notun ortalaması alınıp çıkan sonuç
# 100 90 arası "AA"- 90 80 arası "AB" - 80 70 arası "BB"- 70 60 arası "CB" - 60 50 "CC"
# ekrana yazdır

# vize = int(input("vize: "))
# final = int(input("final: "))

# ortalama = vize*0.4 + final*0.6
# print(ortalama)
# if final>=50:
#    if 100>= ortalama >= 90:
#       print("AA")
#    elif 90> ortalama >= 80:
#       print("BA")
#    elif 80> ortalama >= 70:
#       print("BB")
#    elif 70> ortalama >= 60:
#       print("CB")
#    elif 60> ortalama >= 50:
#       print("CC")
#    else:
#       print("FF")

# ===== ÖDEV =====
# Kullanıcıya sinema ya da tiyatro tercihi sorulsun.
# sinema 20tl tiyatro 10tl öğrenciyse %50 indirim yapılacak emeklliye %25
# tercih, durum, 
# tercih = input("sinema(1) tiyatro(2): ")
# durum = input("hiçbiri(0) öğrenci(1) emekli(2): ")
# if tercih == "1" and durum == "0":
#    print("20₺")
# elif tercih == "1" and durum == "1":
#    print("10₺")
# elif tercih == "1" and durum == "2":
#    print("15₺")
# elif tercih == "2" and durum == "0":
#    print("10₺")
# elif tercih == "2" and durum == "1":
#    print("5₺")
# elif tercih == "2" and durum == "2":
#    print("7,5₺")

# /// iç içe if yapıları
# tercih = input("sinema(1) tiyatro(2): ")
# durum = input("hiçbiri(0) öğrenci(1) emekli(2): ")
# if tercih == "1":
#    if durum == "0":
#       print("20₺")
#    elif durum == "1":
#       print("10₺")
#    elif durum == "2":
#       print("15₺")
# elif tercih == "2":
#    if durum == "0":
#       print("10₺")
#    elif durum == "1":
#       print("5₺")
#    elif durum == "2":
#       print("7,5₺")

# data_user = [
#     {
#       "fname":"Berkay",
#       "username":"berkay111",
#       "password":"111",
#       "email":"berkay@gmail.com",
#       "active" : False,
#     },
#     {
#       "fname":"Tugay",
#       "username":"tugay222",
#       "password":"222",
#       "email":"tugay@gmail.com",
#       "active" : False,
#     }
# ]

# kullanıcı isimlerini ekrana yazdır
# print(data_user[0]["fname"])
# print(data_user[1]["fname"])
# kullanıcı mailini değiştir
# data_user[0]["email"] = "basri@gmail.com"
# print(data_user[0])

# kullanıcıya soyad ekle
# data_user[0]["lname"] = "Ülger"
# print(data_user[0])

# kullanıcı sisteme giriş yapsın
# kullanıcı sisteme giriş yapsın (online olup olmadığını kontrol et)
# kullanıcının şifresini değiştir (doğrulama yaptır)
# username = input("username: ")
# password = input("password: ")

# if data_user[0]["username"] == username and data_user[0]["password"] == password:
#    print("Hoşgeldiniz...", data_user[0]["fname"])
#    data_user[0]["active"] = True
# else:
#    print("Kullanıcı adı veya şifre yanlış!!")


# if data_user[0]["active"] == True:
#    if input("şifre değiştirmek için (1): ") == "1":
#       if data_user[0]["password"] == input("password: "):
#          data_user[0]["password"] = input("Yeni Şifre: ")
# else:
#    print("Giriş Sayfasına Yönlendirilir... Girişli Değil!!")
# print(data_user[0])



# === kullanıcıdan girilen sayi çiftse ekrana çift yazdır tekse tek yazdır. kullanıcıdan girilenin sayı olduğunu kontrol etsin
# s1 = input("s1: ")
# if s1.strip("-").isnumeric():
#    if int(s1)%2 == 0:
#       print("bu sayı çifttir",s1)
#    else:
#       print("bu sayı tekdir",s1)

# === ehliyet alıp alamaması kuralı kullanıcıdan sırasıyla veriler alınıcak
#  yaş tutuyor mu, bu kişi sınavdan geçti mi, ehliyet sınavından geçtimi?
# age = int(input("yaş: "))
# if age>18:
#    sinav = int(input("yazılı sınav: "))
#    if sinav >= 70:
#       dsinav = input("direksyon sınavından geçti(e) kaldı(h): ")
#       if dsinav == "e":
#          print("ehliyet alabilirsiniz")
#       else:
#          print("tekrar deneyin")
#    else:
#       print("Yazılı sınava tekrar girmeniz lazım")
# else:
#    print("yaşınız yetmiyor..")


# hava_durumu = random.choice(hava_liste) rasgele verilen hava durumuna göre ekrana hava durumu yazıcak
# print(random.choices(hava_liste, [6,3,1,1,1], k=24)) # (liste, oran, kaç değişken yazılsın)
# hava_liste = ['güneşli', 'yağışlı', 'karlı', 'bulutlu', 'dolu']
# import random
# hava = random.choice(hava_liste)
# print(hava)
# if hava == hava_liste[0]:
#    text = ["keyfine bak", "hava süper", "dışarı çıkıp eğlen", "yürüme vakti", "evde mi duruyosun hala"]
#    print(random.choice(text))
# elif hava == hava_liste[1]:
#    text = ["şemsiyeni unutma", "sudan çıkmış balık", "ıslanmak için güzel gün", "şeker değilsen erimezsin"]
#    print(random.choice(text))
# elif hava == hava_liste[2]:
#    text = ["yerler kaygan", "kalın giyin", "lapa lapa kar", "kaymak için poşetini unutma"]
#    print(random.choice(text))
# elif hava == hava_liste[3]:
#    text = ["rüzgar var", "güneşimi kayettim", "hanimiş bulutlar", "kapalı hava"]
#    print(random.choice(text))
# elif hava == hava_liste[4]:
#    text = ["evden çıkma", "kalkanları hazırla", "mermi yağmuru", "gitti araba"]
#    print(random.choice(text))



# /// for yapısı
# for(i=0; i<10; i++){}
# print(list(range(0,5,1)))

# list1 = [0,1,2,3,4]
# for i in list1:
#    print(i)
   
# for i in range(0,5,1):
#    print(i)
   
# list2 = ["elma","armut","kiraz","muz"]
# for i in list2:
#    print(i)
   
# for i in range(3,15,2):
#    print("elma")
# print("armut")
# if True:
#    print("kiraz")
   


# 5ten 50ye kadar 3er 3er artan liste oluştur
# print(list(range(5,50,3)))

# # 2 nin 10cu kuvvetini bulan sonucu for döngüsü yardımıyla oluşturun
# x = 1
# for i in range(10): # 0123456789
#    x = x * 2
# print(x)
   
# ödev== bir banka uygulaması yap kullanıcı ve şifre doğrulaması yapılsın eğer doğruysa
# bankaya para yatırıcak mı çekicekmi sorgusu oluşturulsun / anapara = 10000
# eğer para yatırıcaksa para miktarı ne kadar yatırması gerektiğini sorun ve ana parayla bu parayı toplayıp bakiyeyi yazdırın
# eğer para çekicekse para çeksin ve kalan bakiyeyi ekrana yazdırsın

# anapara = 10000
# user = {
#    "username":"berkay111",
#    "password":"111",
# }

# username = input("username: ")
# password = input("password: ")

# if user["username"] == username and user["password"] == password:
#    print("Hoşgeldiniz...")
#    sorgu = input("para yatır(1) para çek(2): ")
#    if sorgu == "1":
#       para = int(input("ne kadar para yatırıcaksınız: "))
#       anapara += para
#    elif sorgu == "2":
#       para = int(input("ne kadar para çekiceksiniz: "))
#       if para <= anapara:
#          anapara -= para
#       else:
#          kredi_sorgu = input("Anaparanızı aştınız. Kredi çekmek için(1)")
#          if kredi_sorgu == "1":
#             kredi = input("""
# 10.000₺ kredi faizi %5 (1)
# 50.000₺ kredi faizi %10 (2)
# 200.000₺ kredi faizi %20 (3)
# """)        
#             if kredi == "1":
#                anapara += 10000
#                faiz = 0.05
#             elif kredi == "2":
#                anapara += 50000
#                faiz = 0.10
#             elif kredi == "3":
#                anapara += 200000
#                faiz = 0.20
#             if para > anapara:
#                print("Anaparanız yetersiz kredi hakkınız dolmuştur")
#             else:
#                anapara -= para
#    else:
#       print("seçiminiz yanlış !!!")
#    print("Anapara: ",anapara)
# else:
#    print("kullanıcı adı veya şifre yanlış !!")


# MARKET UYGULAMASI
# bir meyve listesi olsun, her eleman sırasıyla gelsin ve eğer elmaysa ekrana 15tl armutsa 18tl yazdırsın
# list_meyve = ["elma", "armut", "kiraz", "portakal", "şeftali", "muz"]
# for i in list_meyve:
#    if i == "elma":
#       print(i,"15tl")
#    elif i == "portakal":
#       print(i,"16tl")
      

# meyve listesindeki her meyvenin yanına fiyatlar gelicek şeklinde yazdır. örn: "elma 14tl"
# list_meyve = ["elma", "armut", "kiraz", "portakal", "şeftali", "muz"]
# list_fiyat = ["14", "24", "20", "16", "15", "22"]
# list_mf = []
# for i in range(len(list_meyve)):
#    meyve = "{0} {1}₺".format(list_meyve[i], list_fiyat[i])
#    list_mf.append(meyve)

# oluşturulan yeni listede örn: list_meyve_fiyat = ["elma 14tl", "armut 24tl", "kiraz 20tl"]
# 2kilo elma 3kilo kiraz alıcak ve bunların fiyatını ekrana "2kilo elma 28₺".. şeklinde yazdıran program
# list_meyve = ["elma", "armut", "kiraz", "portakal", "şeftali", "muz"]
# list_fiyat = ["14", "24", "20", "16", "15", "22"]
# list_meyve_fiyat = []
# alis = input("ne alıcaksın: ")
# # # input kg, input meyve, fiyat * kg

# for i in list_mf:
#    if i.find(alis) != -1:
#       kg = int(input("kaç kilo alıcaksın: "))
#       hesap = kg * int(i.split()[1][:-1])
#       print("{}kilo {} {}₺".format(kg,alis,hesap))
#       break
# else:
#    print(alis,"STOKTA YOKTUR")   
   
      
      


# break continue pass
# for i in range(10):
#    pass # daha sonrasından yazılıcak kodlar için şimdilik pass geç, boş bırakılan if for'un hata vermemesi için kullanılır
   
# print("merhaba")

# 1den 100e kadar olan tek sayılar ve çift sayılar, ayrı liste yazılsın
# list_tek = []
# list_cift = []
# for i in range(100):
#    if i%2 == 1:
#       list_tek.append(i)
#    else:
#       list_cift.append(i)
      
# print(list_tek)
# print(list_cift)


# 1den 100e yanızca 5e bölünen sayılar liste içerisine yazılsın
# beslist =[]
# for i in range(1,100,1):
#    if i%5 == 0:
#       beslist.append(i)

# print(beslist)   
# 1den 100e 3 ve 7 bölünen tüm sayılar toplansın
# toplam = 0
# for i in range(1,100,1):
#    if i%3==0 and i%7==0:
#       toplam += i
# print(toplam)


# ==== Alıştırma
# kullanıcı şifre doğrulaması yapan bir sistemde toplam 3 deneme hakkı verilir
# eğer yanlış değerler girilirse parolayı unuttunmu sorusu sorulur hayır derse sistemden çıkılır evet derse
# kayıt olunurken girilen mail adresi ve gizli cevap sorularak parolayı yenileme istenir. parola yenilendikten sonra
# yeni parolayla giriş yapar ve ekrana sisteme giriş yapıldı yazar
# user = [
#    {"fname":"Berkay", "username":"berkay111", "password":"111", "email":"b@", "gizli yanıt":"kedi"},
#    {"fname":"Emre", "username":"emre111", "password":"222", "email":"e@", "gizli yanıt":"köpek"},
# ]

# haklar = [2,1,0]
# for hak in haklar:
#    username = input("username: ")
#    password = input("password: ")
#    if user[0]["username"] == username and user[0]["password"] == password:
#       print("giriş yaptınız")
#       break
#    else:
#       print("kullanıcı adı veya şifre yanlış!!", "kalan hak:",hak)
#       sorgu = input("şifrenizi unuttunuz mu?(e,h)")
#       if sorgu == "e":
#          email = input("email: ")
#          gizli = input("gizli: ")
#          if user[0]["email"] == email and user[0]["gizli yanıt"] == gizli:
#             user[0]["password"] = input("yeni password: ")
#             haklar.append(0)
#             continue
         
#       elif sorgu == "h":
#          continue

# kullanıcı şifre doğrulama sisteminde tüm kullanıcıları kontrol etsin ve sisteme girişini yaptırın
# username = input("username: ")
# password = input("password: ")
# for i in user:
#    if i["username"] == username and i["password"] == password:
#       print("giriş yaptınız",i["fname"])
#       break
# else:
#    print("kullanıcı adı veya şifre yanlış")

# ===== Alıştırma =====
# kullanıcıdan 0ın üstünde bir sayı girilecek girilen sayının 0 dan bu sayıyya kadar olanları
# tek sayıların toplamını yazdır
# çift sayıların toplamını yazdır

# s1 = int(input("s1: "))
# toplamcift = 0
# toplamtek = 0
# if s1>0:
#    for i in range(s1):
#       if i%2 == 0:
#          toplamcift += i
#       else:
#          toplamtek += i
   
#    print("çift toplam:",toplamcift)
#    print("tek toplam:",toplamtek)
# else:
#    print("0dan büyük sayı giriniz..")

      

# 70 sayısı for ile girilicek her sayının
# 5ile bölümünden kalan 1 ise x değişkenine toplasın,
# kalan 2 ise atlasın, 3 ise y değişkenine listelesin
# diğer değerler içinde z içine toplasın
# 60a geldiğinde döngüden çıksın
# x = 0
# y = []
# z = 0
# for i in range(70):
#    if i>=60:
#       break
#    elif i%5==1:
#       x+=i
#    elif i%5 == 2:
#       continue
#    elif i%5 == 3:
#       y.append(i)
#    else:
#      z += i
   
# print(x) 
# print(y) 
# print(z) 

# *************** ===== random.randint for if
# ===== PROJE ===== sayı tahmin oyunu
# while kullanmak yasak
# 1den 100e kadar olan sayılardan
# rastgele verilen sayıyı kullanıcı 6 hakla bulacak


# ***** ekstra senin tuttuğun sayıyı bulmaya çalışsın 8 hak
# siz sayı tutun bilgisayar bulmaya çalışsın
# her tahminden sonra bilgisayara yukarı yada aşağı diyerek yönlendiriceksin


# ======================
# 6 meyve listesi tanımla, 4. elemana kadar ekrana yazdır
# "elma" "armut" son iki harfini çıkar ve aynı listeye tekrar taşı
# meyveler = ["elma","armut","kiraz","muz","kivi","patates"]
# for i in range(len(meyveler)):
#    if i<2:
#       meyveler[i] = meyveler[i][:-2]
#    if i>=4:
#       break
#    print(meyveler[i])

# meyveler = meyveler[:4]
# print(meyveler)


# ÖDEV 100e kadar sayan döngüm olsun bu döngü eğer
# 50.indexin üstünde ve 7ye bölünüyorsa döngü bitsin.
# for 100, 50nin üstünde mi if, if mod 7 bölündüğünde kalan 0 olucak
# for i in range(100):
#    if i>50:
#       if i%7 == 0:
#          print(i)
#          break

# ÖDEV Asal sayıları bulan programı yaz
# 1 ve kendine bölünene asal diyoruz
# bir sayımız olsun, bu sayının hiç bir sayıya bölünmemesi gerekir 1 ve kendisi dışında
# 15 1 ve 15 dışın sayılara bölünmemesini kontrol et
# for tanımla 1in üstünden başlasın ve 15e kadar gitsin, 15in böünmesini kontrol etsin

# nonasal = [] 
# asal = [] 
# for s1 in range(5000,10000):
#    if s1>1:
#       for i in range(2,s1,1):
#          if s1%i == 0:
#             nonasal.append(s1) 
#             break
#       else:
#          asal.append(s1)

# print(nonasal)
# print(asal)



# ÖDEV listede karışık sayılar olucak ve bunların her birine 5 eklenicek
# sonra 3e bölünenlerinden kalanları ve bölüneni ekrana yazdırıcak + eski değerleri
# liste karışık sayı tanımla, listeyi for ile dön ve i 5 ekle,
# i%3, i, i-5

# listkarisik = [11,6,35,24,80,54,41]
# for i in listkarisik:
#    i += 5
#    print("kalan: {} - bölünen: {} - ilk değer: {}".format(i%3, i, i-5) )

# ÖDEV fibonacci sayısı yazdırma
# listenin 2. elemanından başlıcak bir önceki toplanıcak ve listeye eklenicek
# fibo = [1,1]
# for i in range(1000):
#    fibo.append(fibo[i]+fibo[i+1])
   
# print(fibo)


# /// while
# başlangıç
# while (bitiş) (koşul)
# artış

# i=0
# while i<10:
#    print(i)
#    i+=1
   
# while False == 0:
#    print("çıldırdı")

# i=5
# while i<10:
#    print(i)
#    i+=2

# while döngüsü kullanılarak 5e gelince dursun i=0 bitiş 10
# i = 0
# while i<10:
#    print(i)
#    if i>=5:
#       break
#    i+=1


# for yapısını while yapısına dönüştürme
# for döngüsünü sonsuz döngüye sokun
# s1 = [1,2]
# for i in s1:
#    print(i)
#    s1.append(i)


# while döngüsü kullanılcak
# meyve listem olucak içinde meyveler yazsın her birinin önünde "meyve: meyveadı"
# eğer meyve değilse ekrana bu bir meyve değildir yazdırsın
# meyveler = ["elma", 15, "armut", "kiraz", 3]

# i=0
# while i<len(meyveler):
#    if type(meyveler[i]) == str:
#       print(meyveler[i],"meyvedir")
#    i+=1


# Mükemmel sayı, sayılar teorisinde, kendisi hariç pozitif tam bölenlerinin toplamı kendisine eşit olan sayı. 
# Diğer bir ifadeyle, bir mükemmel sayı, bütün pozitif tam bölenlerinin toplamının yarısına eşittir
# s1 = int(input("s1: "))
# for j in range(2,s1):
#    muk = 0
#    for i in range(1,j,1):
#       if j%i==0:
#          muk += i
            
#    if j == muk:
#       print("mükemmel sayıdır", j)

# /// iç içe for yapıları
# for i in range(5): # 0,1
#    for j in range(3):
#       print(j)
# 012012012012

# 1den 5e kadar her sayıyı iki kere yazdıran programı yazdırın
# for i in range(1,5,1):
#    for j in range(2):
#       print(i)

# 0dan 5 kadar olan sayıları 3 kere yazsın ve 3 sayısını yazdırmasın 000 111 222
# for i in range(5):
#    if i != 3:
#       for j in range(3):
#          print(i)

# 0dan 10 kadar olan sayıları 6 kere yazsın ve 5 ve 8 sayısını yazdırmasın
# for i in range(10):
#    if i != 5 and i != 8:
#       for j in range(6):
#          print(i)

# 0dan 10a 123"python" 123 123 şeklinde yazdırsın 4.döngüde dursun

# for i in range(10): # 0 1 2 3
#    if i == 3:
#       break
#    for j in range(1,4):
#       print(j)
#    print("python")




# kullanıcıdan girilen sayının basamak değerini bul

# s1 = 3333333
# print(len(str(s1)))

# girilen cümlede kaç tane a ve e harfi bulunduğunu yazdırın
# text = "bugün arabalara bakmak için evden geldim"
# saye = 0
# saya = 0
# for i in text:
#    if i == "e":
#       saye += 1
#    elif i == "a":  
#       saya += 1

# print("toplam e sayısı",saye)
# print("toplam a sayısı",saya)

# print(text.count("e"))
# print(text.count("a"))

# inputtan cümle alıcaksınız her kelimeyi listeye dönüştürün ve
# listedeki kelimelerde kaç tane a harfi olduğunu yazdırın

# text = "manavdan altı elma aldım birini verdim"
# textlist = text.split(" ")
# for i in textlist:
#    print(i,i.count("a"))


# ============ÖDEV
# kullanıcıdan bir cümle alınsın bunu liste olarak tanımla ve kelime uzunluklarının
# listesini list2 içinde ve ekranda yazdır

# text = input("bir cümle yazınız: ")
# text = text.split(" ")
# list2 = []
# for i in text:
#    list2.append(len(i))

# print(list2)

# ÖDEV=======================
# 10dan 100e kadar 10ar artan bir listeyi her seferinde en sondaki 3 elemanı silip
# ekrana yazdıran ve liste boşalana kadar devam etsin
# list1 = [10,20,30,40...100] ekranda 10dan 100e kadar yazsın
# 3 eleman silindikten sonra 10 20 30 40 50 60 70
# 3 eleman daha silecek ve 10 20 30 40
# 3 eleman daha sil 10
# liste boştur

# list1 = list(range(10,101,10))
# breakbool = False
# for i in range(len(list1)):
#    if breakbool:
#       break
#    for j in range(3):
#       list1.pop()
#       if list1 == []:
#          print("liste boştur")
#          breakbool = True
#          break
#    print(list1)

# for i in range(0,len(list1),3):
#    list1.pop()
#    if list1 == []:
#       print("liste boştur")
#       break
#    list1.pop()
#    list1.pop()
#    print(list1)
   
   # try:
   #    list1.pop()
   #    list1.pop()
   #    list1.pop()
   #    print(list1)
   # except:
   #    print("liste boştur") 



# /// dict 1-ekle 2-çıkar 3-yapıyı değiştir 4-sil 5-temizle 6-for içinde kullanımı
# list1 = ["elma","armut","kiraz"]
# print(list1[2])
# dict2 = {0:"elma", 1:"armut",2:"kiraz"}
# print(dict2[2])

# EKLEME
# dict1 = {"key1":"value1"}
# dict1["key2"] = "value2"
# dict1.update({"key3":"value3", 4:"v4"})
# print(dict1)

# # ÇIKARMA
# dict1.pop("key3") # key değeri seçili olanı çıkartır
# dict1.popitem() # son elemanı ıkartır
# del dict1["key1"]

# print(dict1.get("key1"))
# print(dict1["key1"])

# list1 = [1,2,3,4,5]
# if 0 in list1:
#    print(list1)

# ELEMAN DEĞİŞTİRME
# dict1["key2"] = 2
# dict1.update({ 4:"444", "key1":111 })

# SİL TEMİZLE
# # dict1.clear()
# # del dict1
# print(dict1)

# dict1 = {"k1":"v1","k2":"v2","k3":"v3"}
# for i in dict1.keys():
#    print(i)

# for i in dict1.values():
#    print(i)

# for k,v in dict1.items():
#    print(k,v)
   
# for i in dict1:
#    print(i, dict1[i])

# list1 = ["bir","iki","üç","dört"]
# for i in range(len(list1)):
#    print(i, list1[i])
   
# for i,e in enumerate(list1):
#    print(i,e)
   
   
# araba markası modeli pakedi yılı sonradan girilecektir
# car1 = {}
# car1.update({"marka":"kia", "model":"rio", "paket":"full", "yıl":2017})
# print(car1)

# # # yılı değiştir ekrana yazdır ve sonra sil ekrana yazdır
# car1.update({
#    "yıl":2020
# })
# print(car1)
# car1.pop("yıl")
# print(car1)


# 1den 100e kadar olan asal sayıları list_asal listesine eklesin


# cards = [
#    {"id":0, "title":"Java", "write":"very hard"},
#    {"id":1, "title":"Python", "write":"easy"},
#    {"id":2, "title":"C#", "write":"hard"},
#    {"id":3, "title":"Javascript", "write":"normal"},
#    {"id":4, "title":"Dart", "write":"normal"},
#    {"id":5, "title":"C", "write":"very hard"},
#    {"id":6, "title":"HTML", "write":"very easy"},
# ]

# UYGULAMA
# 1) tanımlı olan kartların zorluk sırasına göre newcards sözlüğüne diziniz 
# 2) id numaralarını tekrar tanımlayın 
# newcards = []
# write = ["very easy","easy", "normal","hard","very hard"]
# newid = 0
# for j in write:
#    for i in cards:
#       print(i.get("write"))
#       if i.get("write") == j:
#          newcards.append(i)
#          i.update({"id":newid})
#          newid+=1
# print(newcards)

# UYGULAMA
# 1) input() kullanıcının arama alanına girdiğini cards içerisinde aratınız ve var olup olmadığı hakkında bilgi yazınız
# 2) örn: arama alanına pyt yazdığında bile bulan bir arama motoru yapınız. 
# search = input("aramak istediğiniz yazınız: ")
# nonsearch = True
# for i in cards:
#    if search.lower() in i.get("title").lower():
#       print("Aradığını bulundu..", i)
#       nonsearch = False
      
# if nonsearch:
#    print("Aradığınız Bulunmuyor!!")

# for i in cards:
#    nonsearch = True
#    for harf in search: # p in pn
#       if harf.lower() not in i.get("title").lower():  # p in python
#          nonsearch = False
#          break
   
#    if nonsearch:
#       print(i)


# ÖDEVVV
# list1 = [1,3,5,7,9,13,15,17]
# # list1 içerisindeki eksik olan tek sayıyı bulduran programı yaz 11 (dinamik olsun)

# ind = 0
# for i in range(1,list1[-1]+1,2):
#    print(i, list1[ind])
#    if i != list1[ind]:
#       print(i)
#       ind -= 1
#    ind += 1
      

# ALIŞTIRMA 
# ogrenciler = {
#     "Python": [{"Çağrı": 60}, {"Hasan": 20}],
#     "Js": [{"Buğra": 90}, {"Hasan": 40}, {"Ayşe":70}],
#     "Php": [{"Çağrı": 30}],
# }
# Sınıfın ortalamasını bulunuz, derslerin ortalaması, 50 ve üstü sınavı geçenler ve kalanlar ayrı olarak listelensin

# ortalama_s = 0
# girilen_s = 0
# ortalama_py = 0
# ortalama_js = 0
# ortalama_php = 0
# gecenler = []
# kalalar = []
# for ders, ogrenci_list in ogrenciler.items(): # 3 
#    for ogrenci in ogrenci_list: # 2,3,1
#       for kisi,note in ogrenci.items(): # 1 1 1 1 1 1 = 6
#          print(kisi, note)
#          if note>=50:
#             gecenler.append({kisi:note,"ders":ders })
#          else:
#             kalalar.append({kisi:note, "ders":ders})
#          girilen_s += 1
#          ortalama_s += note
#          if ders == "Python":
#             ortalama_py += note
#          if ders == "Js":
#             ortalama_js += note
#          if ders == "Php":
#             ortalama_php += note
# ortalama_py = ortalama_py/len(ogrenciler["Python"])
# ortalama_js = ortalama_js/len(ogrenciler["Js"])
# ortalama_php = ortalama_php/len(ogrenciler["Php"])
# ortalama_s = ortalama_s/girilen_s
# print(ortalama_s)
# print("Python dersinin ortalaması: ",ortalama_py)
# print("Js dersinin ortalaması: ",ortalama_js)
# print("PHP dersinin ortalaması: ",ortalama_php)
# print("geçenler:", gecenler)
# print("kalanlar:", kalalar)

# /// dict iç içe yapılar

# basriberkay@gmail.com
# ===== dict ad soyad kullanıcı adı şifre
# 1) kullanıcı şifreyle giriş yapalım ve ad soyadla hoş geldin desin,
# 2) eğerki şifreyi yanlış giriyorsa şifreyi unuttun mu sorulur unuttuysa kullanıcı adı ve gizli yanıt
# kontrolü yapılır doğru bilgileri girdikten sonra şifre değiştirebilir
# 3) değiştirilen şifre ile giriş yapsın

# kul1 = {
#    "ad": "Berkay",
#    "soyad": "Ülger",
#    "kullanıcı adı": "berkay123",
#    "şifre": "111",
#    "gizli": "kedi",
# }
# kul2 = {
#    "ad": "Ali",
#    "soyad": "Kaya",
#    "kullanıcı adı": "ali123",
#    "şifre": "222",
#    "gizli": "köpek",
# }
# kul3 = {
#    "ad": "Veli",
#    "soyad": "Koncuk",
#    "kullanıcı adı": "veli123",
#    "şifre": "1234",
#    "gizli": "anakonda",
# }
# all_kul = [
#    kul1,
#    kul2,
#    kul3,
# ]

# login = False
# while 1:
#    if login:
#       break
   
#    username = input("username: ")
#    password = input("password: ")
#    for user in all_kul:
#       if user["kullanıcı adı"] == username and user["şifre"] == password:
#          print(user["ad"], user["soyad"], "hoşgeldiniz..") 
#          login=True
#          break
#    else:
#       print("kullanıcı adı veya şifre yanlış!!")
#       sorgu = input("şifreyi unuttunuz mu (1,2): ")
#       if sorgu == "1":
#          username = input("Şifreninizi değiştirmek için, username: ")
#          gizli = input("gizli yanıtınız: ")
#          for user in all_kul:
#             if user["kullanıcı adı"] == username and user["gizli"] == gizli:
#                user["şifre"] = input("Yeni şifreniz: ")
#                break
         
#       elif sorgu == "2":
#          pass
#       else:
#          print("yanlış dğer girdiniz!!")

# 

# /// fonksiyonlar def
# 10,20
# 25,50
# 44,22

# def toplamDef(x,y):
#    toplam = x+y
#    print(toplam)
   
# toplamDef(10,20)
# toplamDef(25,50)
# toplamDef(44,22)

# dışardan girilen iki sayıyı önce topla sonra 3 ile çarp , 5 ile modunu al eğer bölünüyorsa böldüm seni yazsın bölünmüyorsa ekrana kalan sayıyı yazdır

# def myDef(s1,s2):
#    toplam = s1 + s2
#    carp = toplam * 3
#    if carp%5==0:
#       return ("Böldüm Seni")
#    else:
#       return (carp%5)
      
# print(myDef(10,225))
# print(myDef(11,22)*2)
# print(myDef(90,5))

# sonuc = 0
# a=10
# def aaA():
#    sonuc=a*5
#    return sonuc

# print(aaA())
# print(sonuc)


# def fonksiyonunda inputtan adımız alıncak ve eğer adımız doğruysa ekrana doğrudur yazdırsın
# data = ["ali","mehmet","ayşe"]
# fname = input("isim gir: ")
# def nameKontrol(name):
#    if name == fname:
#       print("kontrol başarılı...")

# for name in data:
#    nameKontrol(name)


# 1) verilen bir dizi listesinin en uzun karakter sayısını bulun , "elma", "armut" fonksiyon kullanılcak
# 2) sadece bu liste için değil tüm listeler için hesaplasın
# 3) liste içinde sayılar bile olsa hatasız çalışmalı

# def maxLength(liste):
#    uzun = 0
#    for i in liste:
#       if type(i) == list:
#          for i in i:
#             if type(i) == int:
#                i=str(i)
#             if len(i)>uzun:
#                uzun = len(i)
#                eleman = i
         
#       if type(i) == int:
#          i=str(i)
#       if len(i)>uzun:
#          uzun = len(i)
#          eleman = i
      
   
#    return eleman

# meyveler = ["elma", "armut", ["anasımezardikecekmiş", "çarkıfelek"],"ananas", "kiraz", "muz"]
# say = ["bir","iki","üç","dört","bej"]
# print(maxLength(meyveler))
# print(maxLength(say))

# 1) verilen listenin içerisindeki en büyük sayıyı bulun methodsuz
# 2) string ifadeler bile olsa hatasız çalışsın
# list1 = [2,3,4222,1,"asdasd",24422,"asdasd",43333333,22,44]
# def proMax(liste):
#    buyuk = float('-inf') # eksi sonsuz
#    for i in liste:
#       if type(i) == int:
#          if i>buyuk:
#             buyuk=i
#    return buyuk

# list2 = [-22,-2,-11,-5,-50]
# print(proMax(list1))
# print(max(list1))

# print(proMax(list1))


# kullanıcıdan alınan sayı içerisindeki 0dan o sayıya kadar tüm tek sayıların çarpımını yazdıran fonksiyon
# def tekCarpim(sayi):
#    tek = 1
#    for i in range(1,sayi,2):
#       tek *= i
#    return tek

# s1 = int(input("bir sayı giriniz: "))
# print(tekCarpim(s1))


# onclick = myDef(this)
# myDef(e){
#    e
# }
# 1) fonksiyondan 2 değer alınacak girilen aralıktaki asal sayılar ekrana yazdırılsın

# def asalFind(s1,s2):
#    nonasal = []
#    asal = []
#    if s1>s2:
#       s1,s2 = s2,s1
#    for say in range(s1,s2):
#       for i in range(2,say):
#          if say%i == 0:
#             nonasal.append(say)
#             break 
#       else:
#          asal.append(say)
#    return asal


# function def

# def Carpim(x,y):
#    carpim = x*y
#    print(carpim)
   
# Carpim(10,20)

# def Kalan(s1,s2):
#    kalan = s1%s2
#    return kalan
   
# kalan 3E eşitse ekrana elma yazdır
# kalan 5e eşitse ekrana armut yazdır
# diğer kalanlar için ekrana kivi

# sonuc = Kalan(26,7)
# print(sonuc)
# if sonuc == 3:
#    print("elma")
# elif sonuc == 5:
#    print("armut")
# else:
#    print("kivi")

# list1 = [1,2,3,4]
# list2 = ["elma","kiraz","muz"]
# list3 = ["bir","iki","üç"]

# def elemanTopla(arr):
#    for i in arr:
#       print(i)
    
# elemanTopla(list1)
# elemanTopla(list2)
# elemanTopla(list3)

# def ciftBul(arr):
#    cift = []
#    for i in arr:
#       if i%2==0:
#          cift.append(i)
#    return cift
   
# liste içinden en büyük sayıdan en küçük sayıyı çıkarsın
# list1 = [23,55,12,45,68,8,44]
# list2 = [16,9,24,28,40,21,1]

# ciftarr = ciftBul(list2)
# ciftarr.sort()
# print(ciftarr[-1] - ciftarr[0])



# listedeki en uzun eleman ile ek kısa elemanı birleştir örn:abuzettinElma
# arr1 = ["Kavun","Elma","Abuzettin","Ahmet", "Karamurat"]

# def uzunKelime(arr):
#    uzun=0
#    for i in arr:
#       if len(i)>uzun:
#          uzun = len(i)
#          uzunkelime = i

#    return uzunkelime

# def kisaKelime(arr):
#    kisa = float("inf")
#    for i in arr:
#       if len(i) < kisa:
#          kisa = len(i)
#          kisakelime = i
#    return kisakelime

# birlesik = uzunKelime(arr1) + kisaKelime(arr1)
# print(birlesik)


# ÖDEVİ YAPANA 5 puan
# print(text)
# soru = string ifadelere index'e göre ekleme ve çıkarma yapan method tasarla
# text = "bugün bakkala 1 ekmek almaya gittim ama 1 sakız aldım"

# def charAdd(text, ind, char):
#    text = text[:ind] + char + text[ind:]
#    return text


# def charRemove(text,start,end):
#    text = text[:start] + text[end:]
#    return text

# charAdd(text, 20, "lerde")
# charRemove(text, 5, 13)


# /// try except hata algılama

# s1 = "naber"

# try:
#    toplam = int(s1) + 10
#    print(toplam)
# except:
#    print("hata aldınız")


# list1 = [1,2,3]
# list1[5]

# try:
#    toplam = int(s1) + 10
      
#    # sonuc += 15
#    # print(sonuc)
# except NameError:
#    print("değer tanımlı değil")
# except ValueError:
#    s1.count("a")
#    print("değer dönüştürülemedi")
# except TypeError:
#    pass
# except IndexError:
#    pass
# except SyntaxError:
#    pass
# except:
#    print("bir hata alıyosun")

# s1 = 11
# print("pozitif") if s1>0 else print("negatif")

# ALIŞTIRMA =  index methodunu find methoduna dönüştürün
# print("burada index ve find methodu farkını görücez".index("methoduuu"))

# al = "asd"
# text = "elma armut kiraz muz şeftali kayısı"

# def newIndex(text,al):
#    try:
#       sonuc = text.index(al)
#    except:
#       sonuc = -1
#    return sonuc

# print("fınd: ",text.find(al))
# print("newindex: ",newIndex(text,al))

# eğerki içerde yazmıyorsa stokta kalmamıştır

# /// class sınıf yapıları
# class'ın içeriğine istediğimiz zaman ulaşabiliyoruz içerde tanımlanan fonksiyonlar ve içlerindeki değişkenler dahil
# class Toplam:
#    s1 = 15
#    s2 = 20
#    toplam = s1+s2
   
# print(Toplam.s1 + Toplam.s2)
   
# class Toplam:
#    # self: değişkenleri class içinde tanımlı hale getirir, dağıtır yada servis eder
#    def __init__(self, s1,s2): # class'ın ilk çalışan fonksiyonudur, dışardan değişken alabilir
#       self.s1 = s1
#       self.s2 = s2
#       self.toplam = s1+s2

# t1 = Toplam(10,20)


# class BolmeSayı:
#    def __init__(self, s1, s2):
#       self.s1 = s1
#       self.s2 = s2
#       self.sonuc = s1/s2
      
#    def Sonuc(self): # self özelliğini kullanmak çin parantez içine self yazılır
#       print(self.s1/self.s2)
      
# b1 = BolmeSayı(25,7)
# b1.Sonuc()

# class Carpma:
#    def __init__(self, s1, s2):
#       self.s1 = s1
#       self.s2 = s2
#       self.Sonuc()
      
#    def Sonuc(self):
#       print(self.s1*self.s2)

# c1 = Carpma(10,20)
# c2 = Carpma(50,10)
# c3 = Carpma(5,2)
# c4 = Carpma(15,12)


# Şirket personelleri kaydet, ad,maaş,rütbe, özellik
# Maaş giriş yılına göre zam birde özellik zam
# class NeoSirket:
#    tarih = 2023
#    def __init__(self, ad,maas, rutbe, ozellik, basla):
#       self.ad = ad
#       self.maas = maas
#       self.rutbe = rutbe
#       self.ozellik = ozellik
#       self.basla = basla
#       self.ZamBasla()
#       self.Goster()
   
#    def ZamBasla(self):
#       self.calisma = (self.tarih - self.basla)
#       self.maas += self.calisma*300
      
#    def Zam(self, zam):
#       self.maas += zam
#       self.Goster()
      
#    def Goster(self):
#       print(self.maas, self.calisma )

# p1 = NeoSirket("Berkay", 4000, "CEO", "Yakışıklı", 2010)
# p2 = NeoSirket("Sedat", 7000, "Yapımcı", "Yaratıcı", 2015)
# p3 = NeoSirket("Gözde", 9000, "Oyuncu", "Üretken", 2020)

# p1.Zam(600)


# ÖDEV OTOBÜS firmamız olsun firamamıza bilet almak isteyenlerin kaydını yapıyoruz otobüste 50 koltuğumuz var her bilet alan kişi
# için koltuk sayısı azalmalıdır. bilet fiyatı sabit init: ad, koltuk no, tam mı öğrenci mi 
# öğrenciye %20 indirim yapılsın 
# list1 = [22,23,24,25]
# list1.remove(24)

# class NeoBus:
#    firma = "NeoBus"
#    no = list(range(1,51))
#    fiyat = 1000
#    oran = 20/100
#    def __init__(self, ad , koltuk_no, ogrenci):
#       self.ad = ad
#       self.koltuk_no = koltuk_no
#       self.ogrenci = ogrenci
#       if self.Koltuk():
#          self.Durum()
#          self.Print()
      
#    def Koltuk(self):
#       if self.koltuk_no in self.no:
#          self.no.remove(self.koltuk_no)
#          return True
#       else:
#          print("başka koltuk numarası seçiniz", self.no)
#          return False
         
      
#    def Durum(self):
#       if self.ogrenci:
#          self.fiyat = self.fiyat * (1-self.oran)
         
#    def Print(self):
#       print("{}, {} otobüs firmamızdan almış olduğunuz İstanbul - Ankara seferi için bilet numaranız: {} fiyatınız: {}. iyi yolculuklar dileriz".format(self.ad,self.firma,self.koltuk_no, self.fiyat ))
      
      
# b1 = NeoBus("Ahmet", 20, True)
# b2 = NeoBus("Ayşe", 15, False)
# b3 = NeoBus("Fatma", 12, False)
# b4 = NeoBus("Hayriye", 9, True)
# b5 = NeoBus("Hayriye", 32, True)
# b6 = NeoBus("Mahmut", 20, True)


# *************** ===== random.randint for if
# ===== PROJE ===== sayı tahmin oyunu
# while kullanmak yasak
# 1den 100e kadar olan sayılardan
# rastgele verilen sayıyı kullanıcı 6 hakla bulacak


# ***** ekstra senin tuttuğun sayıyı bulmaya çalışsın 8 hak
# siz sayı tutun bilgisayar bulmaya çalışsın
# her tahminden sonra bilgisayara yukarı yada aşağı diyerek yönlendiriceksin

import random

# 1.KISIM
# print("""
# Sayı tahmin oyununa hoşgeldin...
# 1 ile 100 arasında bir sayı tuttum bulmaya çalış.
# """)
# tutulan = random.randint(1,100)
# asagi = ["çok abarttın biraz aşağı", "sallama kardeşim demleme içmiyoruz aşağı..", "küçül biraz", "aşağı in", "bildin.. şaka şaka aşağı."]
# yukari = ["yukarı çık..", "küçülde cebime gir çık yukarı", "sen bilemiceksin çık yukarı","beni yenemezsin yüksel biraz", "ipucu yok"]

# for hak in range(5,-1,-1):
#    tahmin = int(input("Tahmin ettiğin sayı: "))
   
#    if tahmin == tutulan:
#       print("Hayır olamaz nasıl bilebilirsin...")
#       break
#    elif hak==0:
#       print("Kaybettin zaten yenemiyeceğini biliyodum", tutulan)
#       break
#    elif tutulan<tahmin:
#       durum = random.choice(asagi)
#       print("{} kalan hakkınız:{}".format(durum,hak))
#    elif tutulan>tahmin:
#       durum = random.choice(yukari)
#       print("{} kalan hakkınız:{}".format(durum,hak))


# 2.KISIM
# tepe = 100
# alt = 1
# zorluk = input("zorluk derecesi seç:(1,2,3)")
# tahmin_list = []

# if zorluk == "3":
#    print("1den 100'e kadar sayı tut")
#    tepe = 100
# elif zorluk == "2":
#    print("1den 100'e kadar sayı tut")
#    tepe = 100
# elif zorluk == "1":
#    print("1den 200'e kadar sayı tut")
#    tepe = 200

# input("tuttuysan başlayalım enter'a tıkla")
# for hak in range(7,-1,-1):
#    try:
#       if zorluk == "2" or zorluk == "1":
#          tahmin = random.randint(alt,tepe)
#       elif zorluk == "3":
#          tahmin = (alt+tepe)//2
#    except:
#       print("Beni kandırıyosun yalancıııı..., oynama benimle")
#       break
         
#    if tahmin in tahmin_list:
#       print("Beni kandırıyosun yalancıııı..., oynama benimle")
#       break
#    tahmin_list.append(tahmin)
      
   
#    print("tuttuğum sayı:", tahmin)
#    durum = input("bildim mi (evet) bilemediysem aşağı(1) yukarı(2): ")
#    if durum == "evet":
#       print("Yapayzeka dünyayı fetediyor...", tahmin)
#       break
#    elif hak == 0:
#       print("olamaz Kaybettim aferin")
#       break
#    elif durum == "1":
#       tepe = tahmin -1
#    elif durum == "2":
#       alt = tahmin +1



