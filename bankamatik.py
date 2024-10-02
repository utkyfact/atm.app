bakiye = 5000
son_islemler = []
kullanıcı_kaydı = {}

while True:
    kullanıcı_kayıt = input("Kullanıcı adı oluşturunuz: ")

    kullanıcı_sifre = input("Şifrenizi oluşturunuz (sadece rakamlar): ")
    if not kullanıcı_sifre.isdigit():
        print("Şifre sadece rakamlardan oluşmalıdır.")
        continue

    kullanıcı_kaydı[kullanıcı_kayıt] = kullanıcı_sifre
    print("Kullanıcı kaydınız başarıyla oluşturuldu.")
    while True:
        giris1 = input("Kullanıcı adınızı giriniz: ")
        if giris1 in kullanıcı_kaydı:
            giris2 = input("Şifrenizi giriniz: ")
            if kullanıcı_kaydı[giris1] == giris2:
                print("Giriş başarılı!")

                # Banka menüsü
                while True:
                    kullanıcı = int(input("Banker Bilo bankasına hoş geldiniz. \n 1-Bakiye göster. \n 2-Para çek. \n 3-Para yatır. \n 4-Hesap özeti göster. \n 5-Çıkış yap: "))
                    
                    if kullanıcı == 1:
                        print(f"Mevcut bakiyeniz {bakiye} TL.")
                    
                    elif kullanıcı == 2:
                        kacPara = int(input("Kaç para çekeceksiniz? "))
                        if kacPara > bakiye:
                            print("Bakiyeniz yetersiz.")
                        else:
                            bakiye -= kacPara
                            son_islemler.append({"İşlem": "Para çekme", "Miktar": kacPara})
                            print(f"Mevcut bakiyeniz {bakiye} TL.")
                    
                    elif kullanıcı == 3:
                        kacPara = int(input("Kaç para yatıracaksınız? "))
                        bakiye += kacPara
                        son_islemler.append({"İşlem": "Para yatırma", "Miktar": kacPara})
                        print(f"Mevcut bakiyeniz {bakiye} TL.")
                    
                    elif kullanıcı == 4:
                        print("Son işlemleriniz:")
                        for işlem in son_islemler:
                            print(işlem)
                    
                    elif kullanıcı == 5:
                        print("Başarı ile çıkış yaptınız.")
                        break
                    
                   
