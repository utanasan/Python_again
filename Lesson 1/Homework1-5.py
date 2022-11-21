#Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
#финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток
#— издержки больше выручки). Выведите соответствующее сообщение. Если фирма
#отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к
#выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в
#расчете на одного сотрудника.



earnings = float(input("Enter company's earnings "))
outgoings = float(input("Enter company's outgoings "))
if earnings > outgoings:
    print("The company is operating at a profit. Return on revenue amounted to", earnings / outgoings)
    employees = int(input("Enter number of employees "))
    print("Profit per employee was", earnings/ employees)
else:
    print("The company is operating at a loss")