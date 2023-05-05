from calculating_probabilities import prob_freq
bigram_freq = prob_freq
import matplotlib.pyplot as plt

# Разделение биграмм на оси x и вероятностей на оси y
x = list(bigram_freq.keys())
y = list(bigram_freq.values())

# Создание графика
plt.bar(x, y)
plt.xticks(rotation=90)
plt.xlabel('Bigram')
plt.ylabel('Probability')
plt.title('Bigram Frequency Distribution')
plt.show()