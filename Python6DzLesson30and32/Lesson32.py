# Задача 32: Определить индексы элементов 
# массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного 
# минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

n= int(input('Введите количество элементов массива: '))
massiv=list()
for i in range(n):
    e=int(input(f'Введите {i} элемент списка: '))
    massiv.append(e)
print(massiv)
min= input('Введите минимальное значение: ')
min=int(min)
max= input('Введите максимальное значение: ')
max=int(max)
newmassiv=[]
for i in range(len(massiv)):
    if massiv[i] >= min and massiv[i] <= max:
        newmassiv.append(i)
        
print ("Индексы элементов, значения которых принадлежат заданному диапазону: ")
print (newmassiv)