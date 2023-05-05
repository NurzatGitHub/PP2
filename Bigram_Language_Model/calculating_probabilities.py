import json
import pandas as pd
prob_freq = {}
all_bigrams = open('all_bigrams.txt',"r")
all_bg = json.load(all_bigrams)
set_bigrams = set(all_bg)
table_prob = {'quantity':[],'probability':[]}

for bigrams in set_bigrams:
    prob = 0
    table_prob['quantity'].append(f"{bigrams}: {all_bg.count(bigrams)}")
    prob = all_bg.count(bigrams)/len(all_bg)
    table_prob['probability'].append(str("{:.10f}".format(prob)))
    prob_freq[bigrams] = prob

df = pd.DataFrame(table_prob)
df.to_excel('probabilities.xlsx')