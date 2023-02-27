import json
with open("sample-data.json","r") as file:
    data = json.load(file)
    
print(data)
print("""Interface Status
======================================================================================""")
print("""DN                                          Description           MTU      Speed""")
print('''------------------------------------------  ------------------    ----     -------''')

for i in range(3):
    for K, V in data["imdata"][i]['l1PhysIf']["attributes"].items():
        
        if K == 'dn':
            print(V,end="                        ")
        if K == "speed":
            print(V,end="     ")
        if K == 'mtu':
            print(V,end="     ")
    print()

print('\n')