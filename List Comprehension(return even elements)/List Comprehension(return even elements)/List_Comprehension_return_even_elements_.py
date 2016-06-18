import random
def lst_gen():
    lst = random.sample(range(1,1000,1),100)
    print (sorted([even for even in lst if even % 2 == 0]))
lst_gen()
    
    
