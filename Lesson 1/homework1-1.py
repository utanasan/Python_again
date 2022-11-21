#Поработайте с переменными, создайте несколько, выведите на экран, запросите у
#пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

balance = 15
currency_of_balance = 'usd'
print('Your balance is', balance, currency_of_balance)
match = input('Enter sport match ')
bet = int(input('Enter your bet '))
odds = 2
print('You won ', bet*odds)
print('Your balance is', (balance+bet*odds), currency_of_balance)
