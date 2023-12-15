# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: # нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных # границах и пользователь должен угадать 
# # его за заданное число попыток.
# Функция выводит подсказки "больше" и "меньше"
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

import random as rd
from sys import argv # 2 условие в файле

def func(a = 1, b = 10, c = 5): #параметры по умолчанию
  num = rd.randint(a, b)
  for attempt in range(c):
    guess = int(input(f"Попытка N{attempt}: "))
    if guess < num:
      print ("Загаданное число больше.")
    elif guess > num:
      print("Загаданное число меньше.")
    else:
      print("Поздравляю! Вы угадали число!")
      return True
  print("Вы исчерпали все попытки. Загаданное число было: ", num)
  return False

if __name__ == '__main__':
  #temp = [int(i) for i in argv[1: :]] # от терминала придет список с названием 
  #файла и аргументами, аргументы нужно перевести в инт, название убрать с помощью срезов
  print (func(*[int(i) for i in argv[1: :]])) # при таком вызове будет работать как с терминала так и с запуска файла


# Улучшаем задачу 2.
#  Добавьте возможность запуска функции"угадайки" из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: 
# # параметры вызова функции. Для преобразования строковых 
# # аргументов командной строки в числовые 
# # параметры используйте генераторное выражение

#Python3 Task_17_creating_modul.py 2 20 4 команда для запуска с терминала