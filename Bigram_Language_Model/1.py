import torch
# import numpy
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (25.0,7.0)

x_train = torch.rand(1000)
x_train = x_train *50 -25

y_train = torch.cos(x_train)**2
plt.plot(x_train.numpy(),y_train.numpy(),'o')
plt.title('$ cos^2(x) $')
plt.show()