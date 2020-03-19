#Линейный поиск
#Павлюк Владислав,122-В
#Тестирование программы
import numpy as np                  
import random
masiv1=np.array(range(1,15))  #Создадим масив,для проверки правильности нашего поиска.
print(masiv1)                  
x=int(input('Введите элемент который будем искать'))#Если пользователь введет больше 14,соотвественно элемент найден не будет
l=len(masiv1)
count=0                            #Введем счетчик для подсчета количества итераций и перебора нашего масива
while count<l and masiv1[count]!=x:  #Вводим линейный поиск
    count+=1
print('Количество сравнений',count)  #колличество сравнений,начинается с 0 в шаг 1 значение в нашей задаче необходимо х-1 шагов
if count==l:
    print('Елемента нету')  
else:
    print(f'На позиции {count} найден {x}')
#Работа программы с рандомными значениями
masiv2=np.zeros(20,dtype=int)
for i in range(20):
    masiv2[i]=random.randint(-10,10)
print(masiv2)
l1=len(masiv2)
count2=0
while count2<l and masiv2[count2]!=x:  #Вводим линейный поиск
    count2+=1
print('Количество сравнений',count2)  #колличество сравнений
if count2==l1:
    print('Елемента нету')
else:
    print(f'На позиции {count2} найден {x}')
