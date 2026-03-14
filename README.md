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
