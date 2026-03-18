import random

NUM_PRISONERS = 100
MAX_TRIES = 50

# создаем коробки со случайными номерами
boxes = list(range(1, NUM_PRISONERS + 1))
random.shuffle(boxes)

win = True

for prisoner in range(1, NUM_PRISONERS + 1):
    next_box = prisoner

    for attempt in range(MAX_TRIES):
        number = boxes[next_box - 1]

        if number == prisoner:
            print(f"Заключенный {prisoner} нашел свой номер!")
            break
        else:
            next_box = number

        if attempt == MAX_TRIES - 1:
            print(f"Заключенный {prisoner} не нашел свой номер. Все проиграли.")
            win = False
            break

    if not win:
        break

if win:
    print("Все заключенные нашли свои номера. Они выжили!")
else:
    print("Все заключенные погибли.")
import random

boxes = list(range(1, 101))
random.shuffle(boxes)

alive = True

for prisoner in range(1, 101):

    current_box = 101 - prisoner  # зеркальный старт
    found = False

    for step in range(50):

        number = boxes[current_box - 1]

        if number == prisoner:
            print(f"Заключенный {prisoner} нашел свой номер!")
            found = True
            break

        current_box = number

    if not found:
        print(f"Заключенный {prisoner} проиграл. Все погибли.")
        alive = False
        break

if alive:
    print("Все выжили!")
else:
    print("Игра окончена.")
