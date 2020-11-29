import random
from time import sleep

print('Welcome To My Guess The Number Game!')
sleep(2)
print('Try To Guess A Number Between 1, 100!')
sleep(2)
number = random.randint(1, 100)
sleep(1)

trial = 0
for i in range(99999):
    value = int(input("Enter your Guess: "))
    trial = trial + 1
    if value == number:
        print(f'Congrats You"r Correct! at your {trial}. try')
        break
    elif value < number:
      print(f'Try A Bigger Number ! This is you"r  {trial}. try!')
    elif value > number:
      print(f'Try A Smaller Number !This is you"r  {trial}. try!')

print('This Is The End For Now! Have A Great Day And Dont Miss Any Updates ! Please Subscribe To OzGames, It Is My Gaming Channel! https://www.youtube.com/user/amemisoglu')









# print('This Is The 2nd Level Of Guess The Number!')
