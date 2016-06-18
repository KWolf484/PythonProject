import os, re
def txt_file():
    tfile = os.system(r'dir \\TheRig\Movies\ /b > C:/Users/Wolf/Documents/text_files/Movie_list.txt')
    return tfile
txt_file()

def movie_find():
    movie = input('What Movie are you looking for?' )
    tfile = (r'C:/Users/Wolf/Documents/text_files/Movie_list.txt')
    tfile = open(tfile, 'r')
    tfile = tfile.readlines()
    for m in tfile:
        if re.findall(movie, m):
            print (('%s is available') %  movie, )
            print (('Full name: %s') % m, )
        

#movie_find()

def movie_find1():
    movie = input('What Movie are you looking for?' )
    tfile = (r'C:/Users/Wolf/Documents/text_files/Movie_list.txt')
    tfile = open(tfile, 'r')
    tfile = tfile.readlines()
    for m in tfile:
        if re.finditer(movie, m):
            print (('%s is available') %  movie, )
            print (('Full name: %s') % m, )
            
        

movie_find1()
