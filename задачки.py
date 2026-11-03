#часть 1, модули и библиотеки
#2 задача
 
import math #ящик с математическими инструментами

result = math.factorial(10) #сам факториал, считает 1 * 2 * 3... * 10
print("Результат: ", result) #показ ответика

#4 задача

import math #т пифагора с = корень(а2 + b2)

a = 3
b = 4
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2)) #math.pow (a, b, 2) возводит в квадрат, складывая 9 + 16 = 25, math.sqrt(25) берёт корень и даёт результат
print("Гипотенуза равна: ", c)


#9 задача

import math

print(0.1 + 0.2 == 0.3) #false (!) типо дроби хранятся не идеально, 0.1 + 0.2 на самом деле 0.300000 т.д, обычное == говорит не равно
print(math.isclose(0.1 + 0.2, 0.3)) #math.isclose спрашивает они почти одинаковые? и отвечает true

#модули random 

#11 задача

import random

number = random.randint(1, 100) #бросает кубик с гранями от 1 до 100, включая оба края
print("Случайное число: ", number)

#16 задача

import random

numbers = random.sample(range(1, 50), 5) #range даёт числа от 1 до 49, последнее не входит, random.sample достаёт 5 штук без повторов типо как шары из барабана
print("5 уникальных чисел: ", numbers)

#18 задача

import random
import string

def random_password(length):
    symbols = string.ascii_letters + string.digits #ascii_letters это всее латинские, digits это цифры
    password = "" #пустая строка с написанными паролем
    for i in range(length): #цикл lenght раз, каждый раз random.choice берёт один случайный символ, и оно приклеивает его к паролю
        password = password + random.choice(symbols)
    return password

print("Случайный пароль: ", random_password(8))

#модули datetime

#22 задача

import datetime

today = datetime.date.today() #сегодняшняя дата
new_year = datetime.date(today.year + 1, 1, 1) #today.year + 1 это следующий год, а 1, 1 это 1 января, получили дату Нового года
delta = new_year - today #дату можно вычитать, результатом которого будет промежуток времени, и .days будет доставать из него число дней
print(delta.days)


#26 задача

import datetime

today = datetime.date.today()
result = today + datetime.timedelta(days=100) #timedelta(days=100) это отрезок времени длиной 100 дней, дата + отрезок = новая дата
print(result)

#29 задача


import datetime

def is_weekend(date):
    return date.weekday() >= 5 #.weekday() даёт номер дня недели: 0 = понедельник, 1 = вторник, …, 5 = суббота, 6 = воскресенье, если номер 5 или больше это выходной. >=5 даёт True или False и он его возвращает

print(is_weekend(datetime.date(2026, 11, 7)))
print(is_weekend(datetime.date(2026, 11, 3)))


#модули os, sys, time

#31 задача

import os

print(os.getcwd()) #getcwd это get current working directory, то есть где я сейчас нахожусь

#34 задача

import time

for i in range(5, -1, -1): #range(5, -1, -1) якобы начни с 5, иди до -1 не включая его, шагай по -1. в итоге будет 5, 4, 3, 2, 1, 0
    print(i)
    time.sleep(1) #это типо усни на 1 секунду, поэтому числа появляются с паузой

#38 задача

import os

name = "отчёт.docx"
extension = os.path.splitext(name)[1] #splittext разрезает отчёт и docx на две части, [1] берёт вторую часть (.docx) типо расширение
print(extension)

#модуль collections

#39 задача

from collections import Counter

text = "кот пёс кот мышь кот пёс"
words = text.split() #опять же, разрезает слова по пробелам и в случаи чего нам выдается список
counts = Counter(words) #процесс считания что по сколько раз встретилось
print(counts)  # Counter({'кот': 3, 'пёс': 2, 'мышь': 1})

#а дальше меня гонят спать