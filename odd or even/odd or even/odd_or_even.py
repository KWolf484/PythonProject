#This is a App that will ask the user if they would like to either 
#1), Simply find out if a num is odd or even.
#Or
#2), Choose a number and a divider, which will display both the true division (floating point/Decimal) number. 
#As well as the whole number (int) plus any remainder.
#The second option (2) will also, after the inital output (see above) will give the user the option to test the int output and see if it is odd or even.
'''######## Note to self, would like to add functionality so that the user is able to choose whether to test
 the int or float number from the second option (number and divider)######'''
def userInput():
    confirm = 0
    while confirm <= 3:
        ans = input(' Would you like to check if a number is odd or even? \
or to see if a division would produces an even number\n For odd or even type \'1\'\n OR\n \
For divsion of 2 number, and see if the answer is odd or even type \'2\'\n \
Enter here: ').upper
        if ans == '1':
            num = input('Enter a number I will tell you if its odd or even!! ')
            odd_or_even(num)
        elif ans == '2':
            num = input('Please enter the number you would to be divided: ')
            check = input(('Please enter the number you would like to divide %s by: ') % (num))
            divide(num, check)
            return num, check
        else:
            print('Please enter numbers 1 & 2 only!')
            confirm += 1
            continue
    else:
        print ('Too many wrong input types, please run the App again')

def divide(num, check):
    num = int(num)
    check = int(check)
    ansDiv = float(num / check)
    remain = float(num % check)
    print (('%d divided by %d is %.2f , or %.0f with a remainder of %.2f ') % (num, check, ansDiv,ansDiv, remain ))
    print ('would you like to continue and see if the answer is odd or even?')
    ansOOE = input('Yes or No? ').capitalize()
    if ansOOE == 'Yes' or 'Y':
        num = int(ansDiv)
        odd_or_even(num)
        return int(num) 
    else:
        print('Thank you for using my simple APP')

def odd_or_even(num):
    if num >= 1:
            num = int(num)
            if num % 4 == 0:
                print (('The number %d is divisable by the four(4)!!') % (num))
            elif num % 2 != 0:
                print (('The number %d is odd!!') % num)
            elif num % 2 == 0:
                print (('The number %d is even!!') % num)
            else:
                print('Something when wrong!!\nError; Kris you cunt, sort your shite!')
    else:
        print ('Please enter numbers only.')
 
userInput()