


#print ----------------   "isim", "sfafsd", sep="", end=","

"""print('merhaba','Mars', sep=' ',end="\n")
print("merhaba")
print("merhaba"," ","Mars")
###########################################################
def sayiCiftMi(sayi):
      if sayi%2==0:
            print("sayı çifttir")
      else:
            print("sayı tektir")
sayiCiftMi(15)
######################################################################
def yazdir(metin,kacKere):
      for i in range(1, (kacKere+1)):
            print(metin, end='\n')

yazdirilacakMetin=input('yazdırılacak metni giriniz: ')
yazdirmaSayisi=int(input('kaç kez yazdırılsın? : '))
yazdir(yazdirilacakMetin,yazdirmaSayisi)

###########################################################

def faktöriyelAl(sayi):
      sonuc=1
      if (sayi==0 or sayi==1):
            print('sonuç= ', 1)
      elif sayi>1:
            for i in range(1, sayi+1, 1):
                  sonuc*=i

            print('sonuç=', sonuc)

      else:
            print('0 veya daha büyük bir sayısal değer giriniz...')

faktöriyelAl(int(input('faktöriyel alınacak sayıyı girin: ')))

#########################################################################

def agacCiz(agacinYuksekligi, karakter='*'):
      b=agacinYuksekligi
      for i in range(1,agacinYuksekligi+1):
            print(b*' ',(2*i-1)*karakter)
            b-=1

agacYuksekligi=int(input("Ağacın Yükseklik Değerini giriniz: "))
agacKarakteri=input("Ağaç karakterini giriniz: ")

if agacKarakteri !='' and agacYuksekligi >= 1:
      agacCiz(agacYuksekligi,agacKarakteri[0])
elif agacKarakteri =='' and agacYuksekligi >= 1:
      agacCiz(agacYuksekligi)

else: print("Hatalı giriş")
#########################################################################

def faktöriyelAl(sayi):
      sonuc=1
      if (sayi==0 or sayi==1):
            sonuc=1
      elif sayi >1 :
            for i in range(1, sayi+1, 1):
                  sonuc*=i

      else:
            sonuc=-1 # hatalı bir işlem olduğunu anlamak için -1 değerini veriyoruz.

      return sonuc

sonucumuz=faktöriyelAl(9)
if sonucumuz != -1: #hata olup olmadığını kontrol ediyoruz
      print(sonucumuz)
else:
      print('bir hata oluştu')
#######################################################################################

def ortalamaBul(sayilar):
      sayilarinToplamı=0
      sayilarinOrtalamasi=0

      for i in range(len(sayilar)):
            sayilarinToplamı += sayilar[i]
      sayilarinOrtalamasi= sayilarinToplamı/len(sayilar)

      return sayilarinOrtalamasi

sayiAdedi=int(input('kaç adet sayı ortalamasını alacaksınız?: '))
sayilarim=[]

for i in range(0,sayiAdedi):
      print(i+1,'. sayıyı giriniz')

      sayi=int(input())
      sayilarim.append(sayi)
print(ortalamaBul(sayilarim))

#############################################################################

yas=34 #global değişken
dogumGunuMu=True
if dogumGunuMu==True:
      yas +=1  # yerelde (lokal) aynı değişken 1 arttırılmıştır.
      print('Nice Yaşlara! Yaş: ', yas)
####################################################

yas2 = 34 # global bir değişken
dogumGunuMu=False
if dogumGunuMu==True:
      yas2 += 1 # yerel (lokal) aynı değişken 1 arttırılmıştır
      print('Nice Yaşlara! Yaş: ', yas2)

print('yaşınız: ',yas2)
##########################################################
topla=0 # global değişken
def toplamBul(sayiListesi):
      topla =0 # lokal değişken
      for i in range(len(sayiListesi)):
            topla += sayiListesi[i]

      return  topla
print(toplamBul([1,2,3,4,5]))"""


#############################################################


# 11 haneli olmalı
# ilk 10 basamağının toplamının mod 10 u 11. basamağı verir
# her hanesi rakam olmalı
# ilk hanesi 0 olmamalı
# tek hanelerin toplamının 7 katı çift hanelerin ( 0 hariç) toplamını çıkarınca
#elde edilen sonucun mod10 u bize 10. haneyi verir


def isTCID(value):
      value=str(value)
      digits = [int(w) for w in str(value)]

      # 11 haneli olmalı

      if not len(value)==11:
            return False

      #2. şartımız

      if not sum(digits[:10])%10 == digits[10]:
            return False

      #3.Şartımız

      if not value.isdigit():
            return False

      #ilk hanesi 0 olamaz

      if int(value[0])==0:
            return False

      #5. şartımız

      if not (((7*sum(digits[:9][-1::-2]))-sum(digits[:9][-2::-2]))%10)== digits[9]:
            return False

      # Bütün kontroller yapıldı
      return True

value=int(input('TC kimliği giriniz: '))
print(isTCID(value))

############################################################











