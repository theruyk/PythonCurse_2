#Тут неявное преобразование заключается в том что если в списке есть элементы
#то это True, а когда все элементы удалятся и список станет пустым то будет 
# False и цикл while завершится потому что больше не истина.
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
while data:
  print (data.pop())