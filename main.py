import random

boxes = list(range(1, 101))
random.shuffle(boxes)

all_alive = True

for prisoner in range(1, 101):

    found = False

    for box in range(50):
        if boxes[box] == prisoner:
            print(f"Заключенный {prisoner} нашел свой номер в коробке {box+1}")
            found = True
            break

    if not found:
        print(f"Заключенный {prisoner} не нашел свой номер. Все проиграли.")
        all_alive = False
        break

if all_alive:
    print("Все заключенные выжили!")
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
