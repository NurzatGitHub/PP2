import pandas as pd

from bigram_table import all_bigrams
table_prob = {'quantity':[]}

for bigrams in all_bigrams:    
    table_prob['quantity'].append(f"{bigrams}: {all_bigrams.count(bigrams)}")

df = pd.DataFrame(table_prob)

df.to_excel('calculating_probabilities.xlsx',index=False)