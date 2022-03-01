import os
import random
import sys
deste= [2,3,4,5,6,7,8,9,10,20,30,40,50]*4 #4 desteyle oynandıgı için



def el_ver(deste):
    el=[]
    for i in range(2):    # ilk el 2 kağıt verilir
        random.shuffle(deste)
        kart = deste.pop()
        if kart == 20:
            kart = "J"         #BACAK
        if kart == 30:
            kart = "Q"         #KIZ
        if kart == 40:
            kart = "K"         #PAPAZ
        if kart == 50:
            kart = "A"         #AS
        
        el.append(kart)
    return el
        
def puan(el):
    toplam_puan = 0
    for i in el:
         if i == "J" or i == "Q" or i == "K":
            toplam_puan+= 10
         elif i =="A":
             if toplam_puan >10:
                 toplam_puan += 1
             else:
                 toplam_puan += 11
         else:
             toplam_puan += i
    return toplam_puan

def kart_cek(el):
    kart = deste.pop()
    if kart == 20:
        kart = "J"         #BACAK
    if kart == 30:
        kart = "Q"         #KIZ
    if kart == 40:
        kart = "K"         #PAPAZ
    if kart == 50:
        kart = "A"         #AS
    el.append(kart)
    return el



def sonuc(oyuncu,kurpiyer):
    if puan(oyuncu) == 21:
        print("Blackjack yaparak kazandiniz, tebrikler!")
        tekrar_oyna()
    elif puan(kurpiyer) ==21:
        print("Kasa Blackjack yapti, kaybettiniz")
        tekrar_oyna()
    elif puan(kurpiyer) == puan(oyuncu):
        print("Kazanan yok, tur tekrar oynanacak")
        tekrar_oyna()
    
def durma_karsilastirmasi(oyuncu,kurpiyer):
        if puan(oyuncu) == 21:
            if os.name == 'posix':
                 os.system('clear')
            print ("Kagitlariniz :" + str(oyuncu) + " toplami " + str(puan(oyuncu)))
            print("Blackjack yaparak kazandiniz, tebrikler!")
        elif puan(kurpiyer) == 21:
            if os.name == 'posix':
                 os.system('clear')
            print ("Kurpiyer kagitlari :" + str(kurpiyer) + " toplami " + str(puan(kurpiyer)))

            print("Kasa Blackjack yapti, kaybettiniz")

        elif puan(oyuncu) > 21:
            if os.name == 'posix':
                 os.system('clear')
            print ("Kagitlariniz :" + str(oyuncu) + " toplami " + str(puan(oyuncu)))
            print("21'i gecip kaybettiniz.")

        elif puan(kurpiyer) > 21:
            if os.name == 'posix':
                 os.system('clear')
            print ("Kurpiyer kagitlari :" + str(kurpiyer) + " toplami " + str(puan(kurpiyer)))

            print("Kurpiyer 21'i gecti , kazandiniz.")

        elif puan(oyuncu) < puan(kurpiyer):
            if os.name == 'posix':
                 os.system('clear')
            print ("Kagitlariniz :" + str(oyuncu) + " toplami " + str(puan(oyuncu)))
            print ("Kurpiyer kagitlari :" + str(kurpiyer) + " toplami " + str(puan(kurpiyer)))
            print ("Kurpiyerin elindeki puan sizden daha yüksek, kaybettiniz.\n")

        elif puan(oyuncu) > puan(kurpiyer):
            if os.name == 'posix':
                 os.system('clear')
            print ("Kagitlariniz :" + str(oyuncu) + " toplami " + str(puan(oyuncu)))
            print ("Kurpiyer kagitlari :" + str(kurpiyer) + " toplami " + str(puan(kurpiyer)))
            print ("Elinizdeki puan kurpiyerden daha yüksek, kazandiniz.\n")
        elif puan(oyuncu) == puan(kurpiyer):
            if os.name == 'posix':
                 os.system('clear')
            print ("Kagitlariniz :" + str(oyuncu) + " toplami " + str(puan(oyuncu)))
            print ("Kurpiyer kagitlari :" + str(kurpiyer) + " toplami " + str(puan(kurpiyer)))
            print ("Puanlar esit, kazanan yok.\n")
       
def tekrar_oyna():
    tekrar = input("Tekrar oynamak ister misiniz ? (E/H) : ").lower()
    if tekrar == "e":
        kurpiyer = []
        oyuncu= []
        deste= [2,3,4,5,6,7,8,9,10,20,30,40,50]*4
        oyun()
    else:
         sys.exit("Iyi günler dileriz...")  
        
        
def karar_asamasi(oyuncu):
    puanim = puan(oyuncu)
    olumlu = 0
    olumsuz = 0
    total = 0
    for i in deste:
        if i == 20:
            if puanim + 10  >21:
                olumsuz = olumsuz +1
                total = total +1
            else:
                olumlu = olumlu +1
                total = total +1
        elif i == 30:
            if puanim +10  >21:
                olumsuz = olumsuz +1
                total = total +1
            else:
                olumlu = olumlu +1
                total = total +1
        elif i == 40:
            if puanim + 10 >21:
                olumsuz = olumsuz +1
                total = total +1
            else:
                olumlu = olumlu +1
                total = total +1
        elif i == 50:
            if puanim <11:
                if puanim + 10 >21:
                    olumsuz = olumsuz +1
                    total = total +1
                else:
                    olumlu = olumlu +1
                    total = total +1
            else:
                if puanim + 1 >21:
                    olumsuz = olumsuz +1
                    total = total +1
                else:
                    olumlu = olumlu +1
                    total = total +1
        elif i + puanim >21:
            olumsuz = olumsuz +1
            total = total +1
        else:
            olumlu = olumlu +1
            total = total +1
    if total != 0:
        arti_oran = olumlu /total
        eksi_oran = olumsuz /total
    monte_carlo_orani = 0.8                         #Bu oranımızı ben 0.8'e yuvarladım 0.811554371888168 ( Altta testten aldığım bir oran)
    print("Olumlu oranımız:" , arti_oran)
    print("Olumsuz oranımız:" , eksi_oran)
    if arti_oran == 1.0 :
        print("Kesinlikle kart cekmelisin.")
    if eksi_oran == 1.0:
        print("Kesinlike kart cekmemelisin")
    elif eksi_oran < monte_carlo_orani:
        print("Olumlu kart cekme oranın monte carlo test oranına göre yüksek, cekebilirsin")
    elif eksi_oran >= monte_carlo_orani:
        print("Olumlu kart cekme oranın monte carlo test oranına göre düsük, kart cekme")
    # elif arti_oran > eksi_oran:
    #     print("Olumlu kart cekme oranın yüksek, cekmelisin")
    #     #return eksi_oran
    # elif eksi_oran > arti_oran:                               // Bu iki elif ise testsiz, ilk yaptigim kiyasti.
    #     print("Olumlu kart cekme oranın düsük, cekmemelisn")
    #     #return eksi_oran
    else:
        print("Oranlar esit ")
        
def oyun():
    
    oyuncu = el_ver(deste)
    kurpiyer = el_ver(deste)

    print("Kurpiyerin ilk kagidi ",kurpiyer[0])
    print ("Sizin kagitlariniz :" + str(oyuncu) + " toplami " + str(puan(oyuncu)))
    
    secim = "a"
    
    
    while secim != "q":
        karar_asamasi(oyuncu)
        print("Kart cekmek icin (K), durmak icin (D), cikmak icin(Q) giriniz.")
        secim1 = str(input()).lower()
        if secim1 == "k":
            kart_cek(oyuncu)
            print ("Kagitlariniz :" + str(oyuncu) + " toplami " + str(puan(oyuncu)))
            if puan(oyuncu) == 21:
                print("BLACKJACK! Kazandiniz, tebrikler.")
                tekrar_oyna()
            if puan(oyuncu) > 21:
                print("21'i gecip kaybettiniz.")
                tekrar_oyna()
        elif secim1 =="d":
           while puan(kurpiyer)<17:              #oyun kuralı 17den sonra kart çekemez
                kart_cek(kurpiyer)
                print(kurpiyer)
                if puan(kurpiyer)>21:
                    print("Kurpiyer 21'i gecti , kazandiniz.")
                    tekrar_oyna()
           durma_karsilastirmasi(oyuncu,kurpiyer)
           tekrar_oyna()
        elif secim1 == "q":
            print("Bye!")
            secim = "q"              
            sys.exit("Cikis yapildi.")   
oyun()

# def monte_carlo():
#     #Bu testte kumarhanelerin 17'den sonra kurpiyerin kart çekmemesiyle alakalı 
#     #durumların neden olduğunu, asıl riskli oranın ne süreden sonra gerçekleştiğini
#     #öğrenmek ve kurpiyere karşı oynayan elemanımıza da bu oran üzerinden kart çekip çekmemesinin
#     #kıyasını yapmak için bu testi yazdım. 10.000 kere dönen ve ona göre revize edilen destemizin
#     #sonucunda  0.8115543718881687 bu oranı buldum. Kurpiyerin kart çekmediği anlardaki olumsuzluk
#     #oranının ortalaması bu şekilde geliyor.0,5'i geçtiği her andan itibaren kaybetme oranımız
#     #♣daha yüksek fakat ortada dönen büyük bahisleri göz önüne alırsak kesinlikle kart çekmememiz gereken 
#     #durumlar yukarıdaki oranla beraber yaklaşık olarak 0.8'de gerçekleşiyor.    
#
#
#     listem = []
#     for i in range(10000):
#          deste1= [2,3,4,5,6,7,8,9,10,20,30,40,50]*4 
#          oyuncu = el_ver(deste1)
#          kurpiyer = el_ver(deste1)
#          while puan(kurpiyer)<17:              #oyun kuralı 17den sonra kart çekemez               
#                 kart_cek(kurpiyer,deste1)
#          if puan(kurpiyer) <= 21:
#              eksi_oran = karar_asamasi(kurpiyer)
#              if eksi_oran != None:
#                  listem.append(eksi_oran)
#     print("Monte carlo test sonucu: ",sum(listem) / len(listem))
    
    
# monte_carlo()
    
    
    