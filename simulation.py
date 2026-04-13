import pandas as pd
import random

# ---- История игры ----
data = {
    "Раунд": [],
    "Игрок": [],
    "Очки": [],
    "Победа": []
}

players = ["Игрок 1", "Игрок 2"]

# создаём 10 раундов игры
for i in range(1, 11):
    score1 = random.randint(0, 100)
    score2 = random.randint(0, 100)

    winner1 = "Да" if score1 > score2 else "Нет"
    winner2 = "Да" if score2 > score1 else "Нет"

    data["Раунд"].append(i)
    data["Игрок"].append(players[0])
    data["Очки"].append(score1)
    data["Победа"].append(winner1)

    data["Раунд"].append(i)
    data["Игрок"].append(players[1])
    data["Очки"].append(score2)
    data["Победа"].append(winner2)

# создаём таблицу
df = pd.DataFrame(data)

# ---- Вывод истории ----
print("ИСТОРИЯ ИГРЫ:\n")
print(df)

# ---- Статистика ----
print("\nСТАТИСТИКА:\n")

stats = df.groupby("Игрок").agg(
    Всего_раундов=("Раунд", "count"),
    Сумма_очков=("Очки", "sum"),
    Средние_очки=("Очки", "mean"),
    Побед=("Победа", lambda x: (x == "Да").sum())
)

print(stats)

# ---- лучший игрок ----
best_player = stats["Сумма_очков"].idxmax()
print("\n🏆 Лучший игрок:", best_player)
