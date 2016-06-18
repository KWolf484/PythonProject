def less_than():
    print('Enter a number to compair eash list entry to, \
    If the entry is equal to or less that the number you entered, it will be printed as a list')
    userNum = int(input('Enter a number to compair to list: '))
    numlst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    newlst = []

    for n in numlst:
        if n <= userNum:
            newlst.append(n)
       # else:

    print (newlst)

#less_than()
numlst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([n for n in numlst if n <= 5])
