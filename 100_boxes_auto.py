import random

boxes = [random.randint(1, 100) for _ in range(100)]

print("Коробки автоматически заполнены случайными числами:")
for i, val in enumerate(boxes, start=1):
    print(f"Коробка {i}: {val}")