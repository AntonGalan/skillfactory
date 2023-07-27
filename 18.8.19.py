
amount = 0
tickets = int(input("Введите необходимое количество билетов: "))
for age in range(tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        amount += 0
    elif 18 <= age <= 25:
        amount += 990
    elif age > 25:
        amount += 1390
if amount == 0:
    print("Проходите бесплатно на конференцию!")
elif tickets > 3:
        discount = amount / 100 * 10
        print(f"Скидка составляет: {discount} руб.")
        print(f"К оплате с учетом скидки: {amount - discount} руб.")
else:
    print(f"Сумма к оплате: {amount} руб.")