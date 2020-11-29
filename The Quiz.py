from time import sleep

def Question_To_Get_Answer(number, question, answer):
    print(f'{number} Question!')
    sleep(3)
    print(question)
    sleep(1)
    for i in range(7, 0, -1):
        print(f'You Have {i} Seconds Left!')
        sleep(1)

    print(f'Answer:! {answer}')
    print('The Next Question Will Be Up On 5 Seconds!')
    sleep(5)

print('1st Question!')
sleep(3)
print('What Is 7*8?')
sleep(1)
for i in range(7, 0, -1):
    print(f'You Have {i} Seconds Left!')
    sleep(1)

print('Answer:56')
print('The Next Question Will Be Up On 5 Seconds!')
sleep(5)
print('2nd Question!')
print('Im 9 Years Old, How Many Times '
      'Do You Have To Times My Age To Get To My Dads Age And'
      ' How Many More Left? My Dads Age : 41')
sleep(6)
for i in range(7, 0, -1):
    print(f'You Have {i} Seconds Left!')
    sleep(1)

print('Answer:4 Times + 5 ')
print('3rd Question!')
sleep(3)
print('How Many Millions Of People Are On The World?')
sleep(1)
for i in range(7, 0, -1):
    print(f'You Have {i} Seconds Left!')
    sleep(1)

print('Answer:7800  / 7.800 / 7.8k Millions Of People In The World !')
print('The Next Question Will Be Up On 5 Seconds!')
sleep(5)
Question_To_Get_Answer('4th', 'What School Do I Go To? ', 'ISE (International School Eindhoven) ')
Question_To_Get_Answer('5th', 'Is Moto Moto Funny ',
                        'Yes And No But If You Said No Then I Will Eat You When Your Asleep!')
Question_To_Get_Answer('6th', 'How Many Hair Does Blonde People Have?', '150.000 Hair ! WOW MIND BLOWING!')
Question_To_Get_Answer('7th', 'How Many Countries In The World In 2020?', '195 Countries On 2020!')
Question_To_Get_Answer('8th', 'Where Do I Live?', 'I Live In Netherlands,Meerhoven.')
print ('Thanks For Playing My Quiz Even Though I Probably Showed It To You And Have Fun !' )
print('This Is The End For Now! Have A Great Day And Dont Miss Any Updates ! Please Subscribe To OzGames, It Is My Gaming Channel! https://www.youtube.com/user/amemisoglu')


