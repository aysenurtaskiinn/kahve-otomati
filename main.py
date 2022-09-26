import random
import time 

class Starducs():

  def __init__(self, otomat_durum="kapalı", seker_miktari=0, sut_miktari=0, sut_cesidi=["Normal Süt", "Laktozsuz Süt", "Badem Sütü", "Yulaf Sütü"], sut="Normal Süt", kahve_cesitleri=["Caffe Latte", "Flat White", "Ristretto Bianco", "Caffe Mocha", "Macchiato", "Filtre Kahve ", "Türk Kahvesi", "White Hot Chocolate" ], kahve="White Hot Chocolate"):
    self.otomat_durum= otomat_durum
    self.seker_miktari= seker_miktari
    self.sut_miktari= sut_miktari
    self.sut_cesidi= sut_cesidi
    self.sut= sut 
    self.kahve_cesitleri = kahve_cesitleri
    self.kahve = kahve
  
  def otomat_ac(self):
    if (self.otomat_durum == "Açık"):
      print("Otomat açık")
    else: 
      print("Otomat açılıyor.")
      self.otomat_durum = "Açık"
    
  def otomat_kapat(self):
    if (self.otomat_durum == "kapalı"):
      print("Otomat kapalı")
    else: 
      print("Otomat kapanıyor.")
      self.otomat_durum = "kapalı"


  def seker_ayarlari(self):
     while True:
         cevap = input("şekeri azalt: '<'\nşekeri artır: '>'\nÇıkış : çıkış")
         if (cevap == "<"):
           if (self.seker_miktari != 0):
               self.seker_miktari -=1
               print ("şeker miktarı", self.seker_miktari)
         elif (cevap==">"):
           if (self.seker_miktari !=5):
               self.seker_miktari +=1
               print("şeker miktarı",self.seker_miktari)
         else:
           print("Güncellenmiş şeker miktarınız: ",self.seker_miktari)
           break


  def sut_ayarlari(self):
     while True:
         cevap= input("süt miktarını bir derece azalt: '<'\nbir derece arttır artır: '>'\nÇıkış : çıkış")
         if (cevap == "<"):
           if (self.sut_miktari !=0):
               self.sut_miktari -=1
               print ("süt miktarı", self.sut_miktari)
         elif (cevap == ">"):
           if (self.sut_miktari !=5):
               self.sut_miktari +=1
               print("süt miktarı",self.sut_miktari)
         else:
           print("Güncellenmiş süt miktarınız: ",self.sut_miktari)
           break

  def rastgele_sut(self):
      rastgele = random.randint(0,len(self.sut_cesidi)-1)
      self.sut = self.sut_cesidi[rastgele]
      print("Şu anki süt çeşidi: ",self.sut)

  def kahve_ekle(self, kahve_ismi):
     print("Kahve ekleniyor....")
     time.sleep(1)
     self.kahve_cesitleri.append(kahve_ismi)
     print("Kahve Eklendi.....")

  def rastgele_kahve(self):
   rastgele = random.randint(0,len(self.kahve_cesitleri)-1)
   self.kahve = self.kahve_cesitleri[rastgele]
   print("Şu Anki Kahve Çeşidi: ",self.kahve)

  def __len__(self):
      return len(self.sut_cesidi)

  def __str__(self):
      return "Otomat Durumu: {}\nŞeker Miktarı: {}\nSüt Miktarı: {}\nSüt Çeşitleri: {}\nŞu Anki Süt Çeşidi: {}\nKahve Çeşitleri: {}\nŞu Anki Kahve: {}\n".format(self.otomat_durum,self.seker_miktari,self.sut_miktari,self.sut_cesidi,self.sut,self.kahve_cesitleri,self.kahve)
  
arayuz = Starducs()
   
print("""
      Kahve Otomatı Arayüzü
      1- Otomatı Aç
      2- Otomatı Kapat
      3- Kahve Çeşidi Seçme
      4- Kahve Çeşidi Ekleme   
      5- Süt Çeşidi Seçme
      6- Süt Miktarını Ayarlama          
      7- Şeker Miktarını Ayarlama
      8- Otomat Bilgilerini Öğrenme
      Çıkmak İçin "a"ya Basın.
      """)

while True:
      islem = input("İşlemi Seçiniz: ")
      if (islem == "a"):
        print("Program Sonlandırılıyor...")
        break
      elif (islem == "1"):
        arayuz.otomat_ac()
      elif (islem == "2"):
        arayuz.otomat_kapat()
      elif (islem == "3"):
        arayuz.rastgele_kahve()
      elif (islem == "4"):
        print(arayuz.kahve_cesitleri)
        kahve_isimleri = input("Kahve çeşidi isimlerini ',' ile ayırarak girin:")
        kahve_cesitleri = kahve_isimleri.split(",")
        for eklenecekler in kahve_cesitleri:
          arayuz.kahve_ekle(eklenecekler)
        print(kahve_cesitleri)
      elif (islem == "5"):
        arayuz.rastgele_sut()
      elif (islem == "6"):
        arayuz.sut_ayarlari()
      elif (islem == "7"):
        arayuz.seker_ayarlari()
      elif (islem == "8"):
        print(arayuz)
      else:
        print("Geçersiz İşlem......")


menu = {
    "Caffe Latte": {
        "içindekiler": {
            "su": 50,
            "kahve": 18,
            "süt": 0,
        },
        "maliyet": 1.5,
    },
    "Flat White": {
        "içindekiler": {
            "su": 200,
            "süt": 150,
            "kahve": 24,
        },
        "maliyet": 2.5,
    },
    "Ristretto Bianco": {
        "içindekiler": {
            "su": 250,
            "süt": 100,
            "kahve": 24,
        },
        "maliyet": 3.0,
    },
    "Toffee Nut Latte": {
        "içindekiler": {
            "su": 250,
            "süt": 200,
            "kahve": 24,
        },
        "maliyet": 3.5,
    },
     "Caffe Mocha": {
        "içindekiler": {
            "su": 250,
            "süt": 200,
            "kahve": 24,
        },
        "maliyet": 4.0,
    },
    "White Chocolate Mocha": {
        "içindekiler": {
            "su": 250,
            "süt": 100,
            "kahve": 30,
        },
        "maliyet": 4.5,
    },
    "Macchiato": {
        "içindekiler": {
            "su": 250,
            "süt": 100,
            "kahve": 24,
        },
        "maliyet": 3.0,
    },
    "Cappuccino": {
        "içindekiler": {
            "su": 250,
            "süt": 100,
            "kahve": 24,
        },
        "maliyet": 3.0,
    },
    "Caffè Americano": {
        "içindekiler": {
            "su": 250,
            "süt": 150,
            "kahve": 24,
        },
        "maliyet": 3.5,
    },
    "Filtre Kahve": {
        "içindekiler": {
            "su": 250,
            "süt": 0,
            "kahve": 24,
        },
        "maliyet": 3.0,
    },
    "Türk Kahvesi": {
        "içindekiler": {
            "su": 250,
            "kahve": 24,
            "süt": 0,
        },
        "maliyet": 2.0,
    },
    "Classic Hot Chocolate": {
        "içindekiler": {
            "su": 250,
            "süt": 100,
            "kahve": 24,
            "çikolata": 60,
        },
        "maliyet": 7.0,
    },
    "White Hot Chocolate": {
        "içindekiler": {
            "su": 250,
            "süt": 100,
            "kahve": 24,
            "çikolata": 70,
        },
        "maliyet": 8.0,
    },
    "Espresso": {
        "içindekiler": {
            "su": 350,
            "süt": 100,
            "kahve": 24,
        },
        "maliyet": 5.0,
    },
 }
kaynaklar = {
    "su": 300,
    "süt": 200,
    "kahve": 100,
}  
