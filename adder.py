import gates


# calls the functions of gates and adds binary number according to model
# stores sum as list 
def adder(binarynum1,binarynum2):
        sumval=0
        cin=0
        cout=0
        counter=-1
        sumlist=[]
        
        for i in range ( len (binarynum1)):
            #addition is done from right side to index (z) starts from -1     
            x = binarynum1[counter]
            y = binarynum2[counter]
            
            first = gates.XOR (x,y)
            second = gates.NAND (cin,first)
            third = gates.OR (cin , first)
            fourth = gates.AND (second,third)
            sumval = fourth
            fifth = gates.AND (x,y)
            sixth = gates.AND (first, cin)
            seventh = gates.NOR (fifth, sixth)
            eigth = gates.NOT (seventh)
            cout = eigth
            cin = cout
            sumlist.append (sumval)
            counter = counter -1
            
                    
        #reverse the list as final value is taken from left to right
        #numbers are added from right to left 
        rightorder=[]
        rightordercarry=[]
        rev = -1
        for j in range (len (sumlist)):
            rightorder.append(sumlist[rev])
            rev -=1
            
            
        return rightorder
        
