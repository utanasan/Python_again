# 3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = int(input("Enter month number: "))
season = {'Winter': (1, 2, 12),
          'Spring': (3, 4, 5),
          'Summer': (6, 7, 8),
          'Autumn': (9, 10, 11)}

for key in season.keys():
    if month in season[key]:
        print(key)
        break
else:
    print("Try again ")

# OR

list_of_seasons = ['winter', 'spring', 'summer', 'autumn']
if month == 12 or month == 1 or month == 2:
    print(list_of_seasons[0])
elif month == 3 or month == 4 or month == 5:
    print(list_of_seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(list_of_seasons[2])
elif month == 9 or month == 10 or month == 11:
    print(list_of_seasons[3])
else:
    print("Try again")
