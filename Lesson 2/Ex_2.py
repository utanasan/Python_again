# 2) Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input().

size = int(input("Enter list size "))
l = [input("Enter element ") for i in range(0, size)]
print(l)

for j in range(0, size - 1, 2):
    l[j], l[j + 1] = l[j + 1], l[j]
print(l)
