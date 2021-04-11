# Global AI Hub Day 4, Homework 3

# json veri yapısı kullandım.
studentInfos = {"students": []}
gradeList = []
topStudentList = []

for i in range(5):
    student = input(f"{i + 1}. öğrencinin adını ve soyadını giriniz: ")
    midterm = float(input(f"{i + 1}. öğrencinin vize notunu giriniz: "))
    while midterm < 0 or midterm > 100:
        print("Girilen not değeri 0'dan küçük veya 100'den büyük olamaz.")
        midterm = float(input("Lütfen notunuzu tekrar giriniz: "))
    project = float(input(f"{i + 1}. öğrencinin proje notunu giriniz: "))
    while project < 0 or project > 100:
        print("Girilen not değeri 0'dan küçük veya 100'den büyük olamaz.")
        project = float(input("Lütfen notunuzu tekrar giriniz: "))
    final = float(input(f"{i + 1}. öğrencinin final notunu giriniz: "))
    while final < 0 or final > 100:
        print("Girilen not değeri 0'dan küçük veya 100'den büyük olamaz.")
        final = float(input("Lütfen notunuzu tekrar giriniz: "))
    print("\n")
    # Öğrencinin ortalaması hesaplandı.
    passingGrade = midterm * (0.3) + project * (0.3) + final * (0.4)
    gradeList.append(passingGrade)
    # Girilen bilgileri sözlüğe kaydettik.
    studentInfos["students"].append({"student": student, "midterm": midterm, "project": project, "final": final, "passingGrade": passingGrade})

# Notların bulunduğu listeyi büyükten küçüğe sıraladık.    
gradeList.sort(reverse=True)

for grade in gradeList:
    for student in studentInfos["students"]:
        if student["passingGrade"] == grade:
            topStudentList.append(student["student"])

topStudentList = list(zip(topStudentList, gradeList))

print(topStudentList)
