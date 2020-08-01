import random
a = input('Starting point: ')
a = int(a)
b = input('Ending point: ')
b = int(b)
r = random.randint(a, b)

count = 0

while True :
    answer = input('Type a integer :')
    answer = int(answer)
    if answer == r :
        print('You got it!')
        print('Total tried:', count,'times')
        break
    elif answer > r :
        print('Try a smaller one')
        count = count + 1
    else :
        print('Try a bigger one')
        count = count + 1
    print('You have tried', count,'times')
