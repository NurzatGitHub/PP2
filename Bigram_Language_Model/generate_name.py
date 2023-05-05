from bigram_table import all_bigrams
import torch

new_name = ""
for i in range(10):
    while len(new_name) < 6:
        random_index = torch.randint(low=0, high=len(all_bigrams), size=(1,)).item()
        new_name += all_bigrams[random_index]
    print(new_name)