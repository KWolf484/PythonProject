import random
import getpass
print ('Welcome to Rock, Paper or Sissors\nEnter an option.')
user_obj = getpass.getpass('Rock, Paper or Sissors: ').lower()
ai_obj = input('Rock, Paper or Sissors: ').lower()
rps = ('rock', 'paper', 'sissors')
#ai_rps = ['rock', 'paper', 'sissors']
#ai_obj = random.choice(ai_rps)
def rps_game(user_obj, ai_obj):
    counter = 2
    print('Player selected %s ' % user_obj)
    print('Computer selected %s ' % ai_obj)
    condition = user_obj in rps and ai_obj in rps
    if condition == True:
        if user_obj == ai_obj:
            print('Its a draw!')
        elif user_obj == 'rock':
            if ai_obj == 'paper':
                print('You lose!')
            else:
                print('You win!')
        elif user_obj == 'paper':
            if ai_obj == 'sissors':
                print('You lose!')
            else:
                print('You win!')
        elif user_obj == 'sissors':
            if ai_obj == 'rock':
                print('You lose!')
            else:
                print('You win!')
    else:
        print('You did not enter a valid object %s,\nPlease try again.' % str(rps))
        
rps_game(user_obj, ai_obj)