students = [
    {"name": "Анна", "score": 85, "attempts": 2},
    {"name": "Борис", "score": 55, "attempts": 1},
    {"name": "Вера", "score": 90, "attempts": 4},
    {"name": "Глеб", "score": 70, "attempts": 3}
]

students_one = []
for x in students:
    if x['score'] >= 60 and x['attempts'] <= 3:
        students_one.append(x['name'])
print(students_one)
students_two = [x['name'] for x in students if x['score'] >= 60 and x['attempts'] <= 3]
print(students_two)
print(students_one==students_two)
