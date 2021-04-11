# Global AI Hub Day 2, Homework 1 (Second part of the first homework)

n = int(input("1-10 arasında bir sayı giriniz: "))
while n < 0 or n >= 10:
    print("Girdiğiniz değer 1 ile 10 arasında değil.")
    n = int(input("Lütfen 1-10 arasında değer giriniz: "))
print(f"0 ile {n} arasındaki çift sayılar yazdırılıyor:\n")
print("Sayılar: ", end="")
for num in range(n + 1): # Başlangıç değeri default olarak 0, n + 1 yapmamızın sebebi ise n değerinin de dahil olmasının istenmesi.

    if num % 2 == 0:
        print("{}".format(num), end=" ")
