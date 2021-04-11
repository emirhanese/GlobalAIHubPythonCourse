#Global AI Hub Day 2, Homework 1

# Listeyi ikiye bölüp böldüğü kısımları geri döndüren fonksiyon.
def split(a_list, half):

    return a_list[:half], a_list[half:]


n = int(input("Dizinin boyutunu giriniz: "))
myList = []

# round fonksiyonu kullanmamın sebebi dizi tek sayıda elemana sahip ise çoğunluk olan tarafın ikinci yarıya atanmasını istemem.
half = round(n / 2)

for i in range(n):
    num = int(input(f"{i + 1}. elemanı giriniz: "))
    myList.append(num)

# Asıl dizimizin ilk yarısı tempList dizisinde diğer yarısı da tempList2 dizisinde tutuluyor.
tempList, tempList2 = split(myList, half)

print("\nDeğişmeden önce:", myList)

# Eğer dizinin boyutu tek ise ilk yarıya half değerinden daha az değer atanacağı için istediğimiz gibi çıktı alamayız. Bunun için boyutun tek olup olmadığını kontrol etmeliyiz.
if n % 2 == 1:
    myList[:n - half], myList[n - half:] = tempList2, tempList
# Listenin ilk yarısını ikinci yarısı ile, ikinci yarısını da ilk yarısıyla değişme işlemi.
else:
    myList[:half], myList[half:] = tempList2, tempList

print("Değiştikten sonra:", myList)
