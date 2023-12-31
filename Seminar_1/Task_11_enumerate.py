# Функция enumerate() в Python используется для перебора элементов 
# последовательности (например, списка) вместе с их индексами. Она возвращает 
# кортежи, содержащие индекс и соответствующий элемент. В вашем случае, вы 
# используете ее для перебора элементов списка animals.

# Аргументы enumerate():
# iterable (обязательный): Это итерируемая последовательность, которую вы хотите 
# перебрать.

# start (необязательный): Этот аргумент указывает, с какого значения начать 
# нумерацию индексов. По умолчанию start равен 0.

# В вашем коде enumerate(animals, start=1) означает, что вы хотите начать 
# нумерацию с 1. Затем в цикле for каждая итерация возвращает кортеж, 
# состоящий из индекса (с 1, 2, 3 и так далее) и соответствующего элемента из 
# списка animals. Эти значения присваиваются переменным i и animal, и затем они 
# выводятся на экран вместе.

animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']

for i, animal in enumerate(animals, start=1):
    print(i, animal)
