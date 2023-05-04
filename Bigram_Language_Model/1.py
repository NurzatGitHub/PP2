import pandas as pd
names = open("text.txt","r")

bigram_table = {'name':[],'bigram':[],'bigram_freq':[]}

all_bigrams = []

for name in names:
    freq = 1
    # print(name,end="")
    bigram_table['name'].append(name)
    s = ""
    s_freq = ""
    for i in range(len(name)-1):
        bigram = name[i:i+2]
        s += f"{bigram}  "
        all_bigrams.append(bigram)
        if bigram in all_bigrams:
            freq += 1
            # bigram_table['bigram_freq'].append(freq)
        else:
            freq = 1
            # bigram_table['bigram_freq'].append(freq)
        
        s_freq += f"{bigram} : {freq}  "
    bigram_table['bigram_freq'].append(s_freq)


    bigram_table['bigram'].append(s)
# for bigram in bigram_table:
#     print(bigram + ": " + str(bigram_table[bigram]))
df = pd.DataFrame(bigram_table)
# f = open("myfile.csv", "w")
df.to_csv('myfile.csv',index=False)
print(df)