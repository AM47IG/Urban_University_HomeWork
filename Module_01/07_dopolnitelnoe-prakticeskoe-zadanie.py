from statistics import mean

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_ = list(students)
students_.sort()
average_score1 = {}
for i in range(len(students)):
    average_score1[students_[i]] = sum(grades[i]) / len(grades[i])

average_score2 = {k: mean(v) for k, v in zip(sorted(students), grades)}  # Второй вариант
print(average_score1)
print(average_score2)
