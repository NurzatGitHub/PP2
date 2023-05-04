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
        s_freq += f"{bigram} : {freq}   "
    if bigram in all_bigrams:
        freq += 1

    bigram_table['bigram_alternate_meeting'].append(s_freq)
    bigram_table['bigram'].append(s)

df = pd.DataFrame(bigram_table)

df.to_csv('information.csv',index=False)
# print(df)