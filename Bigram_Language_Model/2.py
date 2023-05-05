import torch
import pandas as pd

# Создаем данные
names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
bigram_table = []
for name in names:
    x = torch.arange(len(name)-1)
    bigrams = [name[i:i+2] for i in x]
    bigram_table.append({"name": name, "bigrams": bigrams})

# Создаем DataFrame из данных
df = pd.DataFrame(bigram_table)

# Сохраняем таблицу в файл CSV
df.to_csv("bigram_table.csv", index=False)