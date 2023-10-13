import random

secenek = ["taş", "kağıt", "makas", "kertenkele", "spoke"]
pc_puan = 0
senin_puanin = 0

print("Oyuna hoş geldin! İlk 10 puanı kazanan oyunu kazanır.")

while True:
    pcSecim = random.choice(secenek)
    seninSecim = input("Seçiminizi yapın: (taş, kağıt, makas, kertenkele, spoke) ").lower()
    print("PC'nin seçimi: ", pcSecim)
    print("Senin seçimin: ", seninSecim)

    if pcSecim == seninSecim:
        print("Berabere, puan yok!")
    else:
        if (pcSecim == "taş" and (seninSecim == "makas" or seninSecim == "kertenkele")):
            pc_puan += 1
        elif (pcSecim == "taş" and (seninSecim == "kağıt" or seninSecim == "spoke")):
            senin_puanin += 1
        elif (pcSecim == "kağıt" and (seninSecim == "taş" or seninSecim == "spoke")):
            pc_puan += 1
        elif (pcSecim == "kağıt" and (seninSecim == "makas" or seninSecim == "kertenkele")):
            senin_puanin += 1
        elif (pcSecim == "makas" and (seninSecim == "kağıt" or seninSecim == "kertenkele")):
            pc_puan += 1
        elif (pcSecim == "makas" and (seninSecim == "taş" or seninSecim == "spoke")):
            senin_puanin += 1
        elif (pcSecim == "kertenkele" and (seninSecim == "spoke" or seninSecim == "kağıt")):
            pc_puan += 1
        elif (pcSecim == "kertenkele" and (seninSecim == "taş" or seninSecim == "makas")):
            senin_puanin += 1
        elif (pcSecim == "spoke" and (seninSecim == "taş" or seninSecim == "makas")):
            pc_puan += 1
        elif (pcSecim == "spoke" and (seninSecim == "kertenkele" or seninSecim == "kağıt")):
            senin_puanin += 1
        else:
            print("Yanlış değer girdiniz doğru formatta giriş yapınız!")

    print("Senin puanın: ", senin_puanin)
    print("PC'nin puanı: ", pc_puan)

    if pc_puan == 10:
        print("PC 10 puana ulaştı, kaybettiniz.")
        break
    elif senin_puanin == 10:
        print("10 puana ulaştın. TEBRİKLER, KAZANDIN!")
        break

       
             
                
            
   
            
            
            
    
            
    
    
    
                
            
            
            
        