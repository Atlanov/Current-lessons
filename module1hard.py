print('Grades and students')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
students = list(students)
list.sort(students)
print(students)
final_mark = {students[0]:sum(grades[0])/len(grades[0])}
final_mark.update({students[1]:sum(grades[1])/len(grades[1]),students[2]:sum(grades[2])/len(grades[2])})
final_mark.update({students[3]:sum(grades[3])/len(grades[3]),students[4]:sum(grades[4])/len(grades[4])})
print('GPA:',final_mark)#Метод из Вебинара немного короче, но я выполнил работу до просмотра Вебинара