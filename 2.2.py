#Бинарый поиск
#Павлюк Владислав,122-В
#Тестирование программы
import numpy as np                  
import random
masiv1=np.array(range(1,15))  #Создадим масив,для проверки правильности нашего поиска.
print(masiv1)                  
x=int(input('Введите элемент который будем искать'))#Если пользователь введет больше 14,соотвественно элемент найден не будет
R=len(masiv1)-1 #Конец масива
L,count,k=0,0,0, #Начало масива,счетчик для сравнений,и переменная для позиции числа
flag=False
while L<=R and not flag :
    k=(L+R)//2 #Допустим,если ввести 9,При первой итерации,к=6,при второй к=10 при третей к =8
    count+=1 # введем счетчик для каждого нашего действия
    if masiv1[k]==x:
        flag=True
    elif masiv1[k]<x:
        L=k+1
        count+=1
    else:
        R=k-1
        count += 1
    
if not flag:
    print('Елемента нету')
else:
    print(f'Елемент найден на позиции {k} за {count} сравнений')
#Работа с рандомными значениями 
masiv2=np.zeros(20,dtype=int)
for i in range(20):
    masiv2[i]=random.randint(-10,10)
masiv2=sorted(masiv2)
print(masiv2)
R1=len(masiv2)-1 #Конец масива
L1,count1,k1=0,0,0, #Начало масива,счетчик для сравнений,и переменная для позиции числа
flag1=False
while L1<=R1 and not flag1 :
    k1=(L1+R1)//2
    count1+=1
    if masiv2[k1]==x:
        flag1=True
    elif masiv2[k1]<x:
        L1=k1+1
        count1+=1
    else:
        R1=k1-1
        count1+=2#Количество сравнений
if not flag1:
    print('Елемента нету')
else:
    print(f'Елемент найден на позиции {k1} за {count1} сравнений')



