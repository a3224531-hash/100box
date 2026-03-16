import random

boxes = list(range(1, 101))
random.shuffle(boxes)

game_over = False

for prisoner in range(1, 101):

    choices = list(range(1, 101))
    random.shuffle(choices)

    found = False

    for i in range(50):
        box = choices[i]

        if boxes[box - 1] == prisoner:
            print(f"Заключенный {prisoner} нашел свой номер в коробке {box}")
            found = True
            break

    if not found:
        print(f"Заключенный {prisoner} не нашел свой номер. Все проиграли.")
        game_over = True
        break

if not game_over:
    print("Все заключенные выжили!")
else:
    print("Игра закончилась поражением.")
