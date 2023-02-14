d = {}

class Mybank():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balace = balance
        d[self.owner] = balance
    def ListOfOwners(self):
        """list of owners"""
        for k,v in d.items():
            print(k,v)
    def registration():
        t = input('Creating new acconut, your Login: ')
        d[t] = 0
        Mybank(t,0)
        print('CREATED NEW ACCOUNT. Login:',t,'. Balance:',d[t])
    def Withdrawals(self):
        s = input('Login: ')
        if d.get(s):
            print('withdraw or replenish ?')
            t = input()
            if t == 'withdraw':
                print('How much do you want to withdraw? You have:',d.get(s))
                a = int(input())
                if a > d.get(s):
                    print("you don't have enough money")
                else:
                    print('withdrawed:',a)
                    print('left:',d.get(s) - a)
            elif t == 'replenish':
                print('how much do you want to replenish your bank ?')
                a = int(input())
                print('replenished:',a)
                print('You have:',d.get(s) + a)
        else:
            print('owner not found!')
            print('want to register?')
            s = input()
            if s == 'yes':
                Mybank.registration()
            else:
                bank.Withdrawals()

bank = Mybank('owner1', 1000000)
Mybank('owner2', 2000000)
Mybank('owner3', 3000000)
Mybank('owner4', 4000000)
Mybank('owner5', 5000000)
bank.Withdrawals()