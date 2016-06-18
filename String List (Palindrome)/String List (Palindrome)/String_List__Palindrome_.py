word = input('Enter a word to check if it is a palindrome: ').upper()
def pal_check(word):
    newWord = []
    for char in list(word[::-1]):
        newWord += char
    newWord = ''.join(newWord)
    if newWord == word:
        print ('%s is a palindrome' % word)
    else:
        print ('%s backwards is %s.\nSo %s is not a palindrome' % (word, newWord, word,))

pal_check(word)
