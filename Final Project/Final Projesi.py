import time
import random

"""
This program is written on VSC IDE.
Bu programda 'Kim Milyoner Olmak İster' adlı programdan almış olduğum 10 adet soru bulunmaktadır. Oyunun işleyişi şu şekildedir:

Her soru başında kullanıcıya sahip olduğu joker haklarının bilgisi verilir.

Kullanıcıya herhangi bir joker hakkını kullanmak isteyip istemediği sorulur.
Kullanırsa eğer joker haklarının ne işe yaradığı aşağıda verilmiştir.

X2 jokeri: Kullanıcının bir soru için 2 adet cevap verebilmesini sağlar.
50:50 jokeri: Kullanıcı bu jokeri hangi soruda kullanmış ise o sorunun yanlış olan şıklarından 2'si silinir.
Seyirci jokeri: Belirli bir oranla kullanıcıya rastgele bir şık verilir. (Yanlış yapma ihtimali var.)

Daha sonrasında kullanıcıdan soruya vereceği cevap istenir "Seçiminizi giriniz şeklinde" 
Eğer seçime J veya j girerse istediği joker hakkını kullanabilir eğer varsa.
Daha sonrasında ise yine seçiminizi giriniz şeklinde mesaj gelir ve kullanıcı soruya cevap verir.
Bu programda büyük ve küçük harf duyarlılığı vardır. A veya a kabul edilmektedir.
Her soru 10 puan değerindedir.
Program sonlandığı zaman eğer kullanıcı 50 puan ve altında ise başarısız sayılır, eğer 50 puanın üstündeyse başarılı sayılır.
Ve daha sonrasında kullanıcıya eğer varsa yanlış yaptığı soruları görüntülemek isteyip istemediği sorulur.
Eğer görüntülemek isterse E veya e tuşlarını girmesi gerek, istemezse H veya h girmesi gerek.
Daha sonrasında ise yanlış yaptığı sorular soru numarası ile ekrana yazdırılır ve altlarında ise kullanıcının o soruya verdiği cevap ve onun altında da sorunun doğru cevabı yazmaktadır.

"""

questions = {

    1: {"question": "Hangisi bir 'Narsistik Sayı' değildir ?", "answer": "D", "A": "153", "B": "370", "C": "371", "D": "406", "truthRateList": ["D", "D", "D", "D", "D", "A", "B", "C"], "true": "D"},
    2: {"question": "Bir işin uygun ve kolay olduğunu belirtmek için hangisi söylenir ?", "answer": "C", "A": "Burnuma göre", "B": "Kaşıma göre", "C": "Dişime göre", "D": "Bıyığıma göre", "truthRateList": ["C", "C", "C", "C", "C","A", "B", "D"], "true": "C"},
    3: {"question": "Klasik bir çengel bulmacada, bir kutucukta en fazla kaç soru sorulur ?", "answer": "B", "A": "1", "B": "2", "C": "3", "D": "4", "truthRateList": ["B", "B", "B", "B", "B", "A", "D", "C"], "true": "B"},
    4: {"question": "Hangi meyvenin 'Vaşington' adıyla satılan bir çeşidi vardır ?", "answer": "B", "A": "Nar", "B": "Portakal", "C": "Elma", "D": "Ananas", "truthRateList": ["B", "B", "B", "B", "B", "A", "D", "C"], "true": "B"},
    5: {"question": "'İki dirhem bir çekirdek' ifadesi kimler için kullanılır ?", "answer": "A", "A": "Güzel ve özenli giyinenler", "B": "Az ve seyrek yiyenler", "C": "Boylu ve kilolu olanlar", "D": "Güçlü ve kaslı olanlar", "truthRateList": ["A", "A", "A", "A", "A", "D", "B", "C"], "true": "A"},
    6: {"question": "Genellikle güneşten korunmak için bir yerin üzerine gerilen, bez veya naylondan yapılmış örtüye ne ad verilir ?", "answer": "D", "A": "Laminant", "B": "Marley", "C": "Lambri", "D": "Tente", "truthRateList": ["D", "D", "D", "D", "D", "A", "B", "C"], "true": "D"},
    7: {"question": "'Bezekçi' hangisinin diğer adıdır ?", "answer": "C", "A": "Hattat", "B": "Sarraf", "C": "Nakkaş", "D": "Hallaç", "truthRateList": ["C", "C", "C", "C", "C","A", "B", "D"], "true": "C"},
    8: {"question": "Halk arasında özellikle hangi yağmurun bereket getirdiğine inanılır ?", "answer": "B", "A": "Şubat yağmuru", "B": "Nisan yağmuru", "C": "Haziran yağmuru", "D": "Ağustos yağmuru", "truthRateList": ["B", "B", "B", "B", "B", "A", "D", "C"], "true": "B"},
    9: {"question": "Hangi kelime 'kalınca bükülmüş ipek iplik' anlamına gelir ?", "answer": "D", "A": "İbrik", "B": "İlmik", "C": "Meşin", "D": "İbrişim", "truthRateList": ["D", "D", "D", "D", "D","A", "B", "C"], "true": "D"},
    10: {"question": "Tarih boyunca İngiltere tahtına hangi adda bir kral çıkmamıştır ?", "answer": "A", "A": "Arthur", "B": "Richard", "C": "Henry", "D": "George", "truthRateList": ["A", "A", "A", "A", "A","D", "B", "C"], "true": "A"}

}

# truthRateList seyirci jokeri kullanıldığı zaman seyircilerin rastgele seçim yapacağı bir liste olacak. Belli bir olasılıkla doğru sonucu bulacaklar. Doğru sonucu bulma ihtimalleri daha yüksek.
# Dictionary objesindeki true ise doğru cevabın bulunduğu şıkkı tutuyor.

userPoint = 0
falseQuestions = [] # Kullanıcı eğer bir soruya yanlış cevap verirse, o sorunun numarası bu listeye aktarılır.
givenAnswers = [] # Kullanıcının verdiği cevapları tutan liste
jokers = ["X2", "50:50", "Seyirciye sor"]
doubleAnswer = False # Eğer kullanıcı X2 (2 cevap hakkı) jokerini kullanırsa True değeri alır.
deleted = False # Eğer kullanıcı 50:50 jokerini kullanmışa True değerini alır. (Şık silinecek anlamında)
toBeDeleted = ["A", "B", "C", "D"] # 50:50 jokeri için silinecek şıkları belirlemek için oluşturulmuş dizi. Bu diziden sorunun cevabı olan şıkkı çıkartıp 2 tane random bir seçim yapıyoruz ve gelen 2 şıkkı siliyoruz.
questionX2Used = int # X2 jokerinin kullanıldığı soru numarasını tutan değişken.
temp = [] # 50:50 jokeri kullanıldığında soruda çıkarılan şıkların tuttuğu değerleri tutan liste.
deletedValues = [] # 50:50 jokeri kullanıldığında çıkarılan şıkları tutan liste.

# Yarışmadaki soruları kullanıcıya soran fonksiyon.
def ask(question_number):
    print(f"\nSoru {question_number}: {questions[question_number]['question']}\nA: {questions[question_number]['A']}\nB: {questions[question_number]['B']}\nC: {questions[question_number]['C']}\nD: {questions[question_number]['D']}\n")

def joker(joker_num, question_number):
    global deleted, doubleAnswer, temp
    print(f"********** {jokers[joker_num]} joker hakkınızı kullandınız. **********\n")

    if jokers[joker_num] == "50:50":
        print("Yanlış şıklardan 2'si siliniyor...")
        time.sleep(2)
        deleted = True
        temporary = ""
        if deleted:
            for i in range(2):
                rand = random.choice(toBeDeleted)
                while rand == questions[question_number]["true"] or rand == temporary:
                    rand = random.choice(toBeDeleted)
                temp.append(questions[question_number][rand])
                questions[question_number][rand] = ""
                temporary = rand
                deletedValues.append(rand)
             
            deleted = False
            
    elif jokers[joker_num] == "X2":
        doubleAnswer = True

    else:
        print("Seyircilere soruluyor...")
        time.sleep(3) # Seyircilere sorduktan 3 saniye sonra seyircilerin cevabı görüntülenecek
        audiencesChoice = random.choice(questions[question_number]["truthRateList"]) # Kullanıcının seyirci jokerini kullandığı soruya ait truthRateList'ten rastgele bir seçim yapılıyor.
        print(f"Seyircilerin seçimi: {audiencesChoice} şıkkı\n")
    jokers.pop(joker_num)

# Kullanıcıya yanlış yaptığı soruları gösteren fonksiyon.
def show_false_questions():
    global questionX2Used
    if len(falseQuestions) != 0:
        for i in falseQuestions:
            print(f"{i}. soru görüntüleniyor...")
            time.sleep(3)
            ask(i)
            time.sleep(1)
            if i == questionX2Used:
                print("{}. soruda 'X2' jokerinizi kullandınız. Verdiğiniz cevaplar:".format(i))
                for ans in givenAnswers[i - 1]:
                    if ans != "":
                        print("-", ans)
                    else:
                        print("-", "Herhangi bir cevap vermediniz.")
            else:
                if givenAnswers[i - 1] != "":
                    print("Bu soruya verdiğiniz cevap: {}\n".format(givenAnswers[i - 1]))
                else:
                    print("Bu soruya verdiğiniz cevap: Soruya herhangi bir cevap vermediniz.")
            print(f"Sorunun doğru cevabı: {questions[i]['answer']} ({questions[i][questions[i]['answer']]})\n\n")
    
    else:
        print("Yanlış yaptığınız soru yok.")

# Kullanıcının cevabını girmesini sağlayan fonksiyon.
def get_answer(question_number):
    global userPoint, doubleAnswer, questionX2Used, temp
    isTrue = False # Eğer 50:50 joker hakkı kullanılırsa true değeri alacak.
    answerList = ['J', 'A', 'B', 'C', 'D'] # Eğer kullanıcı bu listede bulunan karakterlerden farklı bir karakter girerse hata mesajı alacak.
    print("Joker hakkınızı kullanmak istiyorsanız 'J' tuşlayınız. Kullanmak istemiyorsanız cevabın şıkkını tuşlayınız.\n")
    answer = input("Seçiminizi giriniz: ")
    while answer.capitalize() not in answerList: # thanks to capitalize method, character in our string's first index becomes uppercase.
        print("Geçersiz karakter girdiniz. Seçiminizi tekrar giriniz: ", end="")
        answer = input()
    if answer == 'J' or answer == 'j':
        if len(jokers) != 0:
            joker_num = int(input("Kullanmak istediğiniz jokerin numarasını giriniz: "))
            while joker_num < 1 or joker_num > len(jokers):
                print("Geçersiz numara girdiniz.")
                joker_num = int(input("Kullanmak istediğiniz jokerin numarasını giriniz: "))
            if jokers[joker_num - 1] == "50:50":
                isTrue = True
            joker(joker_num - 1, question_number) # joker_num - 1 yapmamızın sebebi kullanıcının seçtiği jokerin indis değerinin 1 eksik olması.
            ask(question_number)
            if isTrue:
                for i in range(2):
                    questions[question_number][deletedValues[i]] = temp[i] # 2 şık silindikten sonra kullanıcı yanlış yaptığı soruları görüntülerken bu soruyu da yanlış yapmışsa 2 şık silinmiş hali çıkmaması için bu şekilde sildiğimiz değerleri tekrardan atıyoruz aynı yere.

        else:
            print("Hiçbir joker hakkınız kalmamıştır.\n\n")

        answer = input("Seçiminizi giriniz: ")
        while answer.capitalize() not in answerList or answer.capitalize() == 'J':
            print("Geçersiz karakter girdiniz. Seçiminizi tekrar giriniz: ", end="")
            answer = input()

    # Eğer X2 (Çift cevap hakkı) kullanılmışsa kullanıcıdan 2. cevabı alacak.
    if doubleAnswer:
        answer2 = input("2. cevabınızı giriniz: ")
        answer = (answer, answer2)
        doubleAnswer = False # Gerekli işlemleri yaptıktan sonra doubleAnswer değişkenini False yapıyoruz aksi taktirde diğer sorular için de geçerli olacak yani her soru için kullanıcıdan 2 cevap alacak.
        questionX2Used = question_number
        
    else:
        answer2 = "" # X2 jokeri aktif değilse answer2 değişkenine boş string atanacak.
    givenAnswers.append(answer)

    # questions[question_number]['answer'] in answer yapmamın sebebi X2 kullanıldığı zaman answer değişkeni bir tuple objesi olacak bu yüzden cevabın tuple'ın içinde olup olmadığını kontrol ediyoruz.
    if questions[question_number]['answer'] in answer  or answer2 == questions[question_number]['answer']:
        if questionX2Used == question_number:
            print("Tebrikler soruyu doğru cevapladınız!")
            print(f"Verdiğiniz cevaplardan doğru olanı: {questions[question_number]['answer']} şıkkı\n\n")
        else:
            print("Tebrikler soruyu doğru cevapladınız!\n\n")
        # Kullanıcı soruyu doğru cevapladığı için 10 puan kazandı.
        userPoint += 10

    else:
        print("Maalesef soruyu yanlış cevapladınız.\n\n")
        falseQuestions.append(question_number) # Soru yanlış cevaplandığı için bu listeye ekledik yanlış cevaplanan soruyu.


def menu():
    print("********** BİLGİ YARIŞMASINA HOŞ GELDİNİZ! **********\n\n")
    print("Yarışma 3 saniye içerisinde başlayacaktır.\n\n")
    time.sleep(3)  # Programı 3 saniye bekletir.


# Kullanıcıya sahip olduğu joker haklarını bildiren fonksiyon.
def jokerInfo():
    print("Kalan joker haklarınız:")
    if len(jokers) != 0:
        for i in range(len(jokers)):
            print(f"{i + 1}- {jokers[i]}")
    else:
        print("Hiçbir joker hakkınız kalmamıştır.")


menu()

for i in range(1, 11):
    jokerInfo()
    ask(i)
    time.sleep(0.5)
    get_answer(i)
    if i < 10:
        print("Bir sonraki soruya geçiliyor...\n\n")
        time.sleep(2)

    else:
        print("********** YARIŞMA SONA ERDİ! **********")
        time.sleep(1)
        if userPoint > 50:
            print("Tebrikler yarışmada başarılı oldunuz!\nPuanınız: {}\n\n".format(userPoint))
        else:
            print("Maalesef yarışmada başarısız oldunuz.\nPuanınız: {}\n\n".format(userPoint))

        if userPoint != 100:
            print("Yanlış yaptığınız soruları görüntülemek istiyorsanız 'E', istemiyorsanız 'H' tuşlayınız: ", end="")
            choice = input()

            if choice == 'E' or choice == 'e':
                show_false_questions()
                print("Program sonlandırıldı.")

            elif choice == 'H' or choice == 'h':
                print("Program sonlandırıldı.")
            
            else:
                print("Geçersiz karakter girdiniz.\nProgram sonlandırılıyor...")
        
        else:
            print("Program sonlandırıldı.")
