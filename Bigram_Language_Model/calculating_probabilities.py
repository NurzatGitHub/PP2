import pandas as pd
from bigram_table import all_bigrams
set_bigrams = set(all_bigrams)
table_prob = {'quantity':[],'probability':[]}
probability = 0
for bigrams in set_bigrams:
    table_prob['quantity'].append(f"{bigrams}: {all_bigrams.count(bigrams)}")
    probability = all_bigrams.count(bigrams)/len(all_bigrams)
    table_prob['probability'].append([probability])

df = pd.DataFrame(table_prob)
df.to_excel('probabilities.xlsx')