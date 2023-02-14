def solve(numheads, numlegs):
    if numheads >= numlegs:
        print('no solution')
    else:
        count_chickens = 0
        count_rabbits = 0
        count_rabbits = (numlegs - 2 * numheads)/2
        count_chickens = numheads - count_rabbits
        print('rabbits =',count_rabbits)
        print('chickens =',count_chickens)

head = int(input())
leg = int(input())
solve(head,leg)    