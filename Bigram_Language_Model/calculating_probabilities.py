import pandas as pd
from bigram_table import all_bigrams
set_bigrams = set(all_bigrams)
table_prob = {'quantity':[],'probability':[]}

for bigrams in set_bigrams:
    prob = 0
    table_prob['quantity'].append(f"{bigrams}: {all_bigrams.count(bigrams)}")
    prob = all_bigrams.count(bigrams)/len(all_bigrams)
    table_prob['probability'].append(str("{:.10f}".format(prob)))
# "{:.10f}".format(probability)
df = pd.DataFrame(table_prob)
df.to_excel('probabilities.xlsx')