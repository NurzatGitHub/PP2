import pandas as pd
names = open("text.txt","r")

bigram_table = {'name':[],'bigram':[],'bigram alternate meeting':[]}

all_bigrams = []
# freq = 1
num_bigrams = 0
for name in names:
    # print(name,end="")
    bigram_table['name'].append(name)
    s = ""
    s_freq = ""
    # num_bigrams = 0
    for i in range(len(name)-1):
        bigram = name[i:i+2]
        s += f"{bigram}  "
        # num_bigrams += 1
        all_bigrams.append(bigram)
        freq = all_bigrams.count(bigram)
        s_freq += f"{bigram} : {freq}   "
    if bigram in all_bigrams:
        freq += 1
            # bigram_table['bigram_freq'][num_bigrams]
            # freq = 1
        # else:
        #     freq = 1
            # bigram_table['bigram_freq'].append(freq)
        

    bigram_table['bigram_freq'].append(s_freq)
    bigram_table['bigram'].append(s)
# for bigram in bigram_table:
#     print(bigram + ": " + str(bigram_table[bigram]))
df = pd.DataFrame(bigram_table)
# f = open("myfile.csv", "w")
df.to_csv('myfile.csv',index=False)
print(df)