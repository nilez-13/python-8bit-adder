
def binary (numberint):
        #converts integer number to binary and stores in list
        binary=[]
        remainder=0
            
        for i in range(8) :
            remainder = numberint % 2
            binary.append(remainder)
            numberint = numberint//2
                
        counter=-1
        binarylist=[]
        for j in range (len(binary)):
                binarylist.append(binary[counter])
                counter-=1
            
        return binarylist



def string(binarylist):
        #takes binary list and coverts it to string 
        stringlist=[]
        for k in range (len(binarylist)):
            stringval=str(binarylist[k])
            stringlist.append(stringval)

        number = ''.join(stringlist)
        return number


def decimal(binarylist):
    #takes binary list and converts it into (decimal) integer    
    counter=-1
    total=0
    for l in range (len(binarylist)):
        bit = binarylist[counter]
        total = total + bit*(2**l)
        counter-=1

    return total

