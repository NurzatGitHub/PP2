bigram_freq = {
    'ab': 0.02,
    'bc': 0.05,
    'cd': 0.03,
    'de': 0.01,
    'ef': 0.04,
    'fg': 0.06,
    'gh': 0.02,
    'hi': 0.03,
    'ij': 0.01,
    'jk': 0.02,
    'kl': 0.04,
    'lm': 0.05,
    'mn': 0.02,
    'no': 0.01,
    'op': 0.03,
    'pq': 0.05,
    'qr': 0.04,
    'rs': 0.03,
    'st': 0.02,
    'tu': 0.01,
    'uv': 0.04,
    'vw': 0.03,
    'wx': 0.02,
    'xy': 0.01,
    'yz': 0.02,
}
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