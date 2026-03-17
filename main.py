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
