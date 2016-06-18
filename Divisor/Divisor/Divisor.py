userNum = int(input('Enter a number to find divisors of: '))
def divisor(userNum):
    divisors = []
    for i in range(2,userNum+1):
        if userNum % i == 0:
            divisors.append(i)
            print (divisors)

divisor(userNum)

