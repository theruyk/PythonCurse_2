# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных 
# элементов исходного слиска. Нумерация начинается с единицы.
my_list = [2, 5, 3, 3, 3, 2, 5, 10, 11, 12]
result = []
for k, v in enumerate (my_list, 1):
  if v % 2:
    result.append (k)
print(result)