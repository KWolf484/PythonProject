import os, subprocess

def make_movie_list():
    dirN = os.chdir(r'\\THERIG/Movies/')
    movies = os.listdir(dirN)
    for m in movies:
        return (m)


    

make_movie_list()