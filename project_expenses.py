total = 0

print("Учёт расходов")
print("Вводи суммы расходов. 'q' — выход.\n")

while True:
    value = input("Расход: ")

    if value == "q":
        break

    if not value.replace(".", "", 1).isdigit():
        print("Нужно ввести число.")
        continue

    expense = float(value)
    total += expense

    print(f"Добавлено: {expense}")
    print(f"Всего расходов: {total}\n")

print(f"Итог за сессию: {total}")
