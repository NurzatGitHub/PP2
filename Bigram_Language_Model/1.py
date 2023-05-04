import pandas as pd
names = open("text.txt","r")

bigram_table = {'name':[],'bigram':[]}

for name in names:
    # print(name,end="")
    bigram_table['name'].append(name)
    s = ""
    for i in range(len(name)-1):
        bigram = name[i:i+2]
        s += f"{bigram}-"
    bigram_table['bigram'].append(s)
        # if bigram in bigram_table:
        #     bigram_table[bigram] += 1
        # else:
        #     bigram_table[bigram] = 1

# for bigram in bigram_table:
#     print(bigram + ": " + str(bigram_table[bigram]))
df = pd.DataFrame(bigram_table)
# f = open("myfile.csv", "w")
df.to_csv('myfile.csv',index=False)
print(df)