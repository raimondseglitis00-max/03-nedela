print("=== A daļa — Saraksti ===")

# Izveido sarakstu ar 5+ skaitļiem
numbers = [4, 7, 10, 3, 8]

print("Sākotnējais saraksts:", numbers)

# Pievieno elementu ar append()
numbers.append(12)
print("Pēc append:", numbers)

# Dzēš pēdējo elementu ar pop()
numbers.pop()
print("Pēc pop:", numbers)


# Aprēķina summu ar for ciklu
total = 0
count = 0

for num in numbers:
    total += num
    count += 1

average = total / count

print("Summa:", total)
print("Vidējā vērtība:", average)


# Filtrē sarakstu — tikai pāra skaitļi
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Pāra skaitļi:", even_numbers)


# Demonstrē šķēlumu (slice)

# Pirmie 3 elementi
first_three = numbers[:3]

# Pēdējie 2 elementi
last_two = numbers[-2:]

# Katrs otrais elements
every_second = numbers[::2]

print("Pirmie 3:", first_three)
print("Pēdējie 2:", last_two)
print("Katrs otrais:", every_second)

print("\n=== B daļa — Vārdnīcas ===")

# Izveido vārdnīcu
studenti = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95
}

print("Sākotnējā vārdnīca:", studenti)

# Pievieno jaunu studentu
studenti["Pēteris"] = 88

# Maina esošu atzīmi
studenti["Jānis"] = 78

print("Pēc izmaiņām:", studenti)


# Iterē cauri vārdnīcai
print("\nStudentu atzīmes:")
for name, grade in studenti.items():
    print(name, ":", grade)


# Atrod studentu ar augstāko atzīmi
best_student = None
best_grade = -1

for name, grade in studenti.items():
    if grade > best_grade:
        best_grade = grade
        best_student = name

print("\nLabākais students:", best_student)
print("Augstākā atzīme:", best_grade)


print("\n=== C daļa — Kombinācija ===")

# Saraksts ar vārdnīcām
students = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 72},
    {"name": "Līga", "grade": 95},
    {"name": "Pēteris", "grade": 78},
    {"name": "Laura", "grade": 88}
]

print("Visi studenti:")
for s in students:
    print(s)


# Filtrē tikai studentus ar atzīmi >= 80
good_students = []

for s in students:
    if s["grade"] >= 80:
        good_students.append(s)


print("\nStudenti ar atzīmi >= 80:")

# Izmanto enumerate() un f-strings
for i, s in enumerate(good_students, start=1):
    print(f"{i}. {s['name']} — {s['grade']}")