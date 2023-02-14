import random
def Guess_the_number():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    a = random.choice(list)
    #print(a)
    print('Hello! What is your name?')
    name = input()
    print()
    print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
    cnt = 0
    while True:
        print('Take a guess.')
        num = int(input())
        print()
        cnt += 1
        if num == a:
            print('Good job,'+ name + '! You guessed my number in '+ str(cnt) + ' guesses!')
            break
        elif num > a:
            print('Your guess too high.')
        elif num < a:
            print('Your guess is too low.')
        elif cnt > 7:
            print('loser!')
            break
Guess_the_number()