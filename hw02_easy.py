# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
for i in fruits:
	print(fruits.index(i) + 1, ". ", "{:>30}".format(i))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

firstList = set(input("Введите значения в первый список через запятую (текст в кавычки): "))
secondList = set(input("Введите значени во второй список через запятую (текст в кавычки): "))

total = firstList | secondList

print(total)


# Или
firstTpl = input("Введите значения в первый список через запятую (текст в кавычки): ")
secondTpl = input("Введите значени во второй список через запятую (текст в кавычки): ")

total = set(firstTpl+secondTpl)

print(set(firstList))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = list(input("Введите список целых чисел через запятую: "))

print(type(numbers))

i = 0

for value in numbers:
	if value % 2 == 0:
		numbers[i] = value / 4
	else:
		numbers[i] = value * 2
	i += 1

print(numbers)