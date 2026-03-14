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
