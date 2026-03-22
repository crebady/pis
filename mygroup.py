groupmates = [
    {
        "name": "Дарья",
        "surname": "Киндинова",
        "exams": ["Большие данные", "ППСубдДиЗ", "АИС"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Онищенко",
        "exams": ["Большие данные", "ППСубдДиЗ", "АИС"],
        "marks": [5, 3, 4]
    },
    {
        "name": "Евгений",
        "surname": "Попов",
        "exams": ["Большие данные", "ППСубдДиЗ", "АИС"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Олег",
        "surname": "Закелов",
        "exams": ["Большие данные", "ППСубдДиЗ", "АИС"],
        "marks": [4, 3, 3]
    },
    {
        "name": "Дмитрий",
        "surname": "Козлов",
        "exams": ["Большие данные", "ППСубдДиЗ", "АИС"],
        "marks": [3, 3, 4]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), 
              str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

# Вызов функции для проверки
print_students(groupmates)
def filter_by_avg_mark(students, avg_threshold):
    filtered = []
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        if avg_mark > avg_threshold:
            filtered.append(student)
    return filtered

# Запрос порога у пользователя
threshold = float(input("\nВведите средний балл для фильтрации: "))
filtered_students = filter_by_avg_mark(groupmates, threshold)

print(f"\nСтуденты со средним баллом выше {threshold}:")
if filtered_students:
    print_students(filtered_students)
else:
    print("Таких студентов нет")