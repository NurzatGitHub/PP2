import datetime


x = datetime.datetime.today() - datetime.timedelta(1)

y = datetime.datetime.today()

z = datetime.datetime.today() + datetime.timedelta(1)

print(x.strftime('%d : %m : %Y'))
print(y.strftime('%d : %m : %Y'))
print(z.strftime('%d : %m : %Y'))