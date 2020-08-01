import random
r = random.randint(1, 100)

while True :
    answer = input('Type a integer :')
    answer = int(answer)
    if answer == r :
        print('You got it!')
        break
    elif answer > r :
        print('Try a smaller one')
    else :
        print('Try a bigger one')
