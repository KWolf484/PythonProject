#returns a list that contains only the elements that are common between the lists (without duplicates). 
print ('returns a list that contains only the elements\nthat are common between the lists (without duplicates). ')
import random
lista = []
listb = []
endlist = [] 
def randlist_gen(z):
    b = random.randrange(1,100,1)
    while b > len(z):
        a = random.randint(1,100)
        z.append(a)
    return (z) 

def list_overlap(a1, a2):
    for char in lista:  
        if char in endlist:
            None
        elif char in a2:
            endlist.append(char)  
    print ('endlist %s' % sorted(endlist)) 
      
lista = randlist_gen(lista)
listb = randlist_gen(listb)
list_overlap(lista, listb)
print ('lista %s' % sorted(lista))
print ('listb %s' % sorted(listb))

#print (newlist, a in )