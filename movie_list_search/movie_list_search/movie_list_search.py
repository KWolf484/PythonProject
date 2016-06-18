import os
#file version 16/11/2015 @ 15:00
#path = 'c:/Users/Wolf/Documents/Text_files'
#os.chdir(path)
#print(os.getcwd())
#print (os.getcwd())
#file = open('movie_list.txt')
#print(file.read())
#movie_list = movie_list.txt
def dirChange():
    path = ('c:/Users/Wolf/Documents/Text_files/')
    os.chdir(path)
    return cwd
    tv = path + 'tv_shows.txt'
    m = path + 'movie_list.txt'
    file = open('movie_list.txt', 'rt')
def media_selection():
    print ('TV Shows(TV) \nMovies (M)')
    user_request = input('What are you looking for? ').lower()
    if user_request == 'm':
        media_file = input('What is the Movie call? ')
        movie = file.readlines()
        if media_file in movie:
            print ('%s - Available!' % media_file )
            file.close()
        else:
            print ('%s - Not available! \nPlease make a request.' % media_file)
            media_selection()
    elif user_request == 'tv':
        print ('TV Shows coming soon!')
        file.close()
        media_selection()
    else:
        print ('Invalid user input \n(Error 000484)')
        file.close()

media_selection()

