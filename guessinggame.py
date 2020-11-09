import random 
print('numberguessinggame')
number = random.randint(1,9)
chance = 0
print('guess a number between 1 and 9')
while chance < 5 :
    guess=int(input('enter your guess'))
    if guess == number:
        print('congratulaions!! U won')
        break
    elif guess < number :
        print('your number is too low')
    else :
        print('guess was too high')
    chance+=1
if not chance < 5:
    print('U loose,the number is ',number)