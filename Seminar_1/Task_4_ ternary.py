# ТЕРНАРНЫЙ ОПЕРАТОР
# result_if_true if condition else result_if_false

# 1)Сначала вы задаете условие (condition), которое будет проверяться. Это выражение 
# должно возвращать булево значение (True или False).
# 2)Затем, после ключевого слова if, вы указываете значение (result_if_true), 
# которое будет возвращено, если условие истинно (True).
# 3)После ключевого слова else, вы указываете значение (result_if_false), которое 
# будет возвращено, если условие ложно (False).
# 4)Затем, в зависимости от результата проверки условия, тернарный оператор
# возвращает либо result_if_true, либо result_if_false.

# my_math = int(input('2 + 2 = '))
# if 2 + 2 == my_math:
#     print('Верно!')
# else:
#     print('Вы уверены?')

# Или используя тернарный оператор:
my_math = int(input('2 + 2 = '))
print('Верно!' if 2 + 2 == my_math else 'Вы уверены?')



# Високосность года

# year = int(input('Введите год: '))
# result = 'YES' if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) else 'NO'
# print(result)