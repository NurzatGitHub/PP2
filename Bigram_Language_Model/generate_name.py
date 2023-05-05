import torch
import json
all_bigrams = open('all_bigrams.txt',"r")
all_bg = json.load(all_bigrams)
new_name = ""

while len(new_name) < 6:
    random_index = torch.randint(low=0, high=len(all_bg), size=(1,)).item()
    all_bg[random_index] = all_bg[random_index].replace('\n','')            
    new_name += all_bg[random_index]
print(new_name)