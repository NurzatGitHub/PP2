import torch
import pandas as pd
names = open("text.txt","r")
bigram_table = {'name':[],'bigram':[],'bigram_alternate_meeting':[]}
all_bigrams = []

num_bigrams = 0
for name in names:
    bigram_table['name'].append(name)
    s = ""
    s_freq = ""
    for i in range(len(name)-1):
        bigram = name[i:i+2]
        s += f"{bigram}  "
        all_bigrams.append(bigram)
        freq = all_bigrams.count(bigram)
        s_freq += f"{bigram}: {freq}   "
    if bigram in all_bigrams:
        freq += 1

    bigram_table['bigram_alternate_meeting'].append(s_freq)
    bigram_table['bigram'].append(s)

# info = ""
# for bigrams in all_bigrams:
#     info = f"{bigrams}: {all_bigrams.count(bigrams)}"
#     bigram_table['all_bigrams'].append(info)

df = pd.DataFrame(bigram_table)
df.to_excel('bigram_table.xlsx',index=False)
# print(df)