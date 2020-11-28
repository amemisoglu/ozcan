import random
from time import sleep

print('Welcome To My Guess The Number Game!')
sleep(2)
print('Try To Guess A Number Between 1, 10 And You Have 5 Seconds To Write Your Guess !')
sleep(2)
number = random.randint(1, 10)
sleep(1)

for i in range(99999):
    value = int(input("Enter your Guess: "))
    if value == number:
        print('Congrats You"r Correct!')
        break
    elif value < number:
      print('Try A Bigger Number !')
    elif value > number:
      print('Try A Smaller Number !')

# print ('This Is The 2nd Level Of Guess The Number!')
