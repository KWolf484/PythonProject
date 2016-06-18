#An app which take user input of name and age, 
#then returns name and the year which they will turn 100. . . .
import datetime
def user_input():
    name = input('What is your name? ' )
    if name.isalpha() == False:
        print('Name must be alphabetical characters only.')
        user_input()
        return name
    else:
        print ('Hello %s ' % (name,))
        age = input('How old are you? ')
        if age.isdigit() == False:
            print ('Age must be numerectical characters only.')
            user_input()
            return age
        else:
            age = int(age)
            now = datetime.datetime.now()
            year = now.year - age + 100
            print ('Hey %s did you know you will turn 100 in the year %s ?' % (name, year))
user_input()