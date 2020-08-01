import random
r = random.randint(0, 100)

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
