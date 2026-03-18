import random

NUM_PRISONERS = 100
MAX_TRIES = 50

boxes = list(range(1, NUM_PRISONERS + 1))
random.shuffle(boxes)

alive = True

for prisoner in range(1, NUM_PRISONERS + 1):

    opened = set()

    for i in range(MAX_TRIES):

        choice = random.randint(1, 100)

        while choice in opened:
            choice = random.randint(1, 100)

        opened.add(choice)

        if boxes[choice - 1] == prisoner:
            print(f"Заключенный {prisoner} нашел свой номер!")
            break

        if i == MAX_TRIES - 1:
            print(f"Заключенный {prisoner} не нашел номер. Все проиграли.")
            alive = False

    if not alive:
        break

if alive:
    print("Все заключенные выжили!")
else:
    print("Все заключенные погибли.")
import random

success = True

for prisoner in range(1, 101):

    boxes = list(range(1, 101))
    random.shuffle(boxes)

    attempts = 0
    found = False

    while attempts < 50:
        choice = random.randint(0, 99)

        if boxes[choice] == prisoner:
            print(f"Заключенный {prisoner} нашел свой номер!")
            found = True
            break

        attempts += 1

    if not found:
        print(f"Заключенный {prisoner} проиграл. Все погибли.")
        success = False
        break
import random

boxes = list(range(1, 101))
random.shuffle(boxes)

def prisoner_turn(prisoner):
    opened = 0
    checked = []

    while opened < 50:
        box = random.randint(1, 100)

        if box not in checked:
            checked.append(box)
            opened += 1

            if boxes[box - 1] == prisoner:
                return True

    return False


all_win = True

for prisoner in range(1, 101):

    result = prisoner_turn(prisoner)

    if result:
        print(f"Заключенный {prisoner} нашел свой номер")
    else:
        print(f"Заключенный {prisoner} проиграл")
        all_win = False
        break


if all_win:
    print("Все заключенные выжили!")
else:
    print("Все заключенные погибли.")

if success:
    print("Все заключенные спаслись!")
else:
    print("Игра окончена.")
import random

boxes = list(range(1, 101))
random.shuffle(boxes)

success_count = 0

for prisoner in range(1, 101):

    attempts = 0
    opened = set()

    while attempts < 50:

        box = random.randint(1, 100)

        if box not in opened:
            opened.add(box)
            attempts += 1

            if boxes[box - 1] == prisoner:
                success_count += 1
                print(f"Заключенный {prisoner} нашел номер")
                break

    else:
        print(f"Заключенный {prisoner} проиграл")
        break

print(f"Всего успешно: {success_count} из 100")

if success_count == 100:
    print("Все выжили!")
else:
    print("Все погибли.")
