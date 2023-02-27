from datetime import datetime,time
d1 = datetime.strptime('2023-02-23 00:00:00',"%Y-%m-%d %H:%M:%S")
print(d1)
d2 = datetime.now().replace(microsecond=0)
print(d2)
print("%s seconds" %((d2 - d1).days*24*3600 + (d2 -d1).seconds))