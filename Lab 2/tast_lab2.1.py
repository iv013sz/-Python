money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
remaining_money = money_capital - spend

while remaining_money >= 0:
    remaining_money += salary
    remaining_money -= spend
    spend += spend * increase
    months += 1
print("Количество месяцев, которое можно протянуть без долгов:",months)

