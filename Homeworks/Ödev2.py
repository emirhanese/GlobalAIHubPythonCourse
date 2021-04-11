# Global AI Hub Day 3, Homework 2

# Kalıcı database için json veri tipi ile de veritabanı oluşturulabilir. Benzer yapıdalar.
# Burada kullandığımız database kalıcı değildir. Sadece program işleyişi boyunca bilgileri tutar.
database = {"users": []}

# Kullanıcının yeni kayıt oluşturmasını sağlar.
def register():
    username = input("Kullanıcı adınızı giriniz: ")
    password = input("Şifrenizi giriniz: ")
    if not is_registered(username):
        # Yeni kaydı veritabanına kaydediyoruz.
        database["users"].append({"username": username, "password": password})
        print("Hesabınız başarıyla oluşturuldu.\n")
    else:
        print("Girdiğiniz kullanıcı adı ile daha önceden kayıtlı hesap bulunmaktadır. Başka bir kullanıcı adı seçiniz.\n")


def delete_user():
    is_deleted = False

    if len(database["users"]) != 0:
        username = input(("Silmek istediğiniz kullanıcının kullanıcı adını giriniz: "))
        if is_registered(username): # Girilen kullanıcı adı ile veritabanına kayıtlı hesap olup olmadığını kontrol ediyoruz.
            password = input("Silmek istediğiniz kullanıcının şifresini giriniz: ")

            # İlk önce girilen bilgilerin hangi kullanıcıya ait olduğu bulunur ve daha sonra o kullanıcı listeden silinir.
            for user in database["users"]:
                if user["username"] == username and user["password"] == password:
                    database["users"].remove(user)
                    print("Kullanıcı başarıyla silindi !\n")
                    is_deleted = True

            if not is_deleted:
                print("Girdiğiniz kullanıcı adı veya şifre yanlıştır. Lütfen daha sonra tekrar deneyiniz.\n")

        else:
            print("Veritabanında girdiğiniz kullanıcı adına ait hesap bulunamadı.\n")

    else:
        print("Henüz veritabanına kayıtlı hiçbir hesap bulunmamaktadır.\n")

        
# Girilen bilgilerin doğru olup olmadığını kontrol eden fonksiyon
def is_true(username, password):
    for user in database["users"]:
        if user["username"] == username and user["password"] == password:
            return True

    print("Girdiğiniz kullanıcı adı veya şifre yanlış.\n")

    return False

# Veritabanında girilen kullanıcı adına ait bir kayıt olup olmadığını kontrol eder ve ona göre boolean değer döndürür.
def is_registered(username=str):
    for user in database["users"]:
        if user["username"] == username:
            return True

    return False

# Veritabanındaki kullanıcıları görüntüler.
def show_users():
    if len(database["users"]) == 0:
        print("Henüz veritabanına kayıtlı herhangi bir kullanıcı yok.\n")

    else:
        print("\nKullanıcılar listeleniyor...")
        for user in database["users"]:
            print("------------------------------\nKullanıcı adı: {}\nŞifre: {}".format(
                user["username"], user["password"]))

        print("\n")

# Kullanıcının sisteme giriş yapabilmesini sağlar.
def login():
    if len(database["users"]) == 0:
        print("Veritabanında henüz kayıtlı hesap bulunmamaktadır. Lütfen yeni kayıt oluşturunuz.\n")
        register()

    else:
        username = input("Kullanıcı adınızı giriniz: ")
        password = input("Şifrenizi giriniz: ")

        checker = is_registered(username)

        if checker:
            if is_true(username, password):
                print(
                    f"Merhaba {username}, Sisteme başarıyla giriş yaptınız.\n")

        else:
            print("Veritabanında bu kullanıcı adında kayıtlı bir hesap bulunamadı.\n")


def menu():
    print("********** Sisteme Hoş Geldiniz. **********\n")
    print("Yapmak istediğiniz işlemi seçiniz:\n1- Giriş yap\n2- Kayıt ol\n3- Kayıtlı hesapları görüntüle\n4- Hesap sil\n5- Çıkış")
    choice()

# Programı sonlandırma fonksiyonu.
def end():
    print("Program sonlandırıldı.")
    # Programı sonlandıran fonksiyon.
    exit(1)

# Kullanıcının seçim girmesini sağlayan fonksiyon.
def choice():
    choice = input("Seçiminizi giriniz: ")

    if choice == "1":
        login()

    elif choice == "2":
        register()

    elif choice == "3":
        show_users()

    elif choice == "4":
        delete_user()

    elif choice == "5":
        end()
    
    else:
        print("Geçersiz karakter girdiniz.\n")
        choice()


while True:
    menu()
