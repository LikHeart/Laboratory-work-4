grades = [2, 5, 2, 5]
count = 1
for grade in grades:
        print(f'{count}: {grade}')
        count += 1
print("----")
for i, grade in enumerate(grades, start=1):
    print(f'{i}: {grade}')
