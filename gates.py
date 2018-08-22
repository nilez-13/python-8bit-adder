# the functions act as logic gates for binary values 
def AND (x,y):
    if x==1 and y==1 :
        return 1
    else :
        return 0
def XOR (x,y):
    if x==y :
        return 0
    else :
        return 1

def OR (x,y):
    if x== 0 and y == 0 :
        return 0
    else :
        return 1
            
def NOT(x):
    if x == 0 :
        return 1
    else :
        return 0

def NOR (x,y):
    if x== 0 and y == 0 :
        return 1
    else :
        return 0
            
def NAND (x,y):
    if x==1 and y==1 :
        return 0
    else :
        return 1
