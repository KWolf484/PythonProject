import os



class movie_finder:
    def __init__(self, movie_name):
        self.movie_name = movie_name
        movie_name = input('Enter Movie name: ')
        os.chdir('C:/Users/Wolf/Documents/Text_files/')
        cwd = (os.getcwd())
        print (cwd + '\\')
        fil = open('movie_list.txt')
        lineCount = 0
        for iline in fil.readlines():
            if iline.startswith(movie_name):
                print ('Yes, %s is available.' % movie_name)
                break
            elif movie_name != fil.readlines():
                lineCount += 1
                print ('No %s' % str(lineCount))
        
            else:
                print('Custom Error: No loop')

 
