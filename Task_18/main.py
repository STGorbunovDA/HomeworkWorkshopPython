# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

lst = [int(i) for i in input("Массив: ").split()]
search_number = int(input("Введи число: "))
number = 0
min_diff = max(lst)
for i in range(len(lst)):
    difference = search_number - lst[i]
    if difference < 0:
        difference *= -1;
    if min_diff > difference:
        min_diff = difference
        number = i
print(f'Самый близкий по величине элемент списка заданному числу {lst[number]}')