__author__ = 'Нагорный Максим Александрович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

import random

number = str(random.randint(0, 1000000000000))
for i in number:
    print(i)



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

n = input("Введите значение для переменной n: ")
d = input("Введите значение для переменной d: ")

v = d
s = n

print("n =", v, "d =", s)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Сколько вам лет? "))

if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данными ресурсом только с 18 лет")

