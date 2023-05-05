import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
import json
a = open('prob_freq.txt',"r")
prob_freq = json.load(a)

# Создание словаря биграмм и соответствующих им вероятностей
bigrams = []
probabilities = []
for key, value in prob_freq.items():
    bigrams.append(key)
    probabilities.append(value)

# Создание входных и выходных данных
X = []
y = []
for i in range(len(bigrams)):
    X.append([ord(bigrams[i][0]), ord(bigrams[i][1])])
    y.append(probabilities[i])
X = np.array(X)
y = np.array(y)

# Создание и компиляция модели
model = Sequential()
model.add(LSTM(32, input_shape=(2, 1)))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

# Обучение модели на выборке
model.fit(X.reshape((len(X), 2, 1)), y, epochs=1000, batch_size=10, verbose=0)

# Тестирование модели
test_input = np.array([[ord('a'), ord('a')]])
predicted_output = model.predict(test_input.reshape((1, 2, 1)))
print('Predicted probability of next bigram:', predicted_output[0][0])
