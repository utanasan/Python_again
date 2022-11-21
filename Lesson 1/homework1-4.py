#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

number = input('Enter integer ')
m = max([int(i) for i in str(number)])
print(m)

#OR

numb = int(input('Enter number '))
maximum = -1
while numb > 10:
    d = numb % 10
    numb = numb//10
    if d > maximum:
        maximum = d
print(maximum)