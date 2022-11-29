# 4) Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
# только первые 10 букв в слове.

entered_string = input("Enter string: ")
splited_list = entered_string.split(' ')
print(splited_list)
for count, item in enumerate(splited_list):
    if len(item) >= 10:
        item = item[0:10]
    print(count, item)
