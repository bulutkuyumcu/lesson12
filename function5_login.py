# Veritabanı
dbUsername = "admin"
dbPassword = "123456"

# Tek bir hesap varmış gibi simüle
def checkPassword(password):
    print("Şifre kontrol ediliyor..")
    if dbPassword == password:
        return True
    else:
        return False

while True:
    username = input("Kullanıcı adınızı giriniz: ")
    if username == dbUsername:
        password = input("Şifrenizi giriniz: ")
        if checkPassword(password) == True: # Fonksiyondan gelen sonuca göre
            print("Giriş başarılı")
            break
        else:
            print("Şifreniz hatalı")
            continue
    else:
        print("Hesap bulunamadı")
        continue