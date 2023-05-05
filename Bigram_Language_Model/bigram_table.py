import json
import pandas as pd
names = open("names.txt","r")
bigram_table = {'name':[],'bigram':[],'bigram_alternate_meeting':[]}
all_bigrams = []

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

df = pd.DataFrame(bigram_table)
df.to_excel('bigram.xlsx')

b = json.dumps(all_bigrams)
f = open("all_bigrams.txt", "w")
f.write(b)
# print(df)