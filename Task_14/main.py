# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
# превосходящие числа N.

n = int(input())
i = 0
while i**2 <= n:
    if i!=0:
        print(i**2)
        i += 1
    else:
        i += 1
        continue
        
    
