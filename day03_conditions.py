age_input = input("Сколько тебе лет? ")

if not age_input.isdigit():
    print("Нужно ввести число.")
else:
    age = int(age_input)

    if age < 18:
        print("Ты несовершеннолетний.")
    elif age < 65:
        print("Ты взрослый человек.")
    else:
        print("Ты пенсионер.")
