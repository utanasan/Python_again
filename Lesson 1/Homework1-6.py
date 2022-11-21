#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
#километров. Каждый день спортсмен увеличивал результат на 10 % относительно
#предыдущего. Требуется определить номер дня, на который результат спортсмена составит
#не менее b километров. Программа должна принимать значения параметров a и b и выводить
#одно натуральное число — номер дня.

first_day_result = int(input("Enter first day result in km "))
overall_result = int(input("Enter overall desired result in km "))
days = 1
km = first_day_result
while km < overall_result:
        first_day_result = 1.1 * first_day_result
        days = days + 1
        km = km + first_day_result
print("The day of your success is", days)