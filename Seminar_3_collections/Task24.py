pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}') # формат 2 знака после запятой

data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
  print(f' {item:>10}') # отступ справа 10 знаков(Выравнивание по правому краю)

num = 2 * pi * data[1]
print(f' {num = :_}') # "num = " разбиение числа на группы по 3 цифры разделяя их "_"