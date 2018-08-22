import converter
import adder
import check

#answer is set to y to loop program as long as user enters y/Y
ans = "y"
while ans == "y":
    print ("---------------------------------------------------------------------------")
    number1 = (input ("enter a number from 0-127 "))
    number2 = (input ("enter a number from 0-127 "))
    print ("----------------------------------------")

    #calls function in check module to see if value is null or not
    nullcheck1 = check.null(number1)
    nullcheck2 = check.null(number2)

    if nullcheck1 == "ok" and nullcheck2 == "ok":#condition which determines both variables have values 
        
    
        numberlist = list(number1)
        numberlist2 = list(number2)

        #calls function in check module to see if there are any aplhabets or characters 
        stringcheck = check.check(numberlist)
        stringcheck2 = check.check(numberlist2)
        
        if stringcheck == "ok" and stringcheck2 == "ok":#condition which determines both values are numeric
            numberint1= int (number1)
            numberint2 = int (number2)
        
        
            if numberint1>=0 and numberint1<=127 and numberint2>=0 and numberint2<=127:#condtion set to accept only values between 0 -127
                sumlist=[]

                #calls function in converter module to convert number to binary
                binarynum1 = converter.binary(numberint1)
                binarynum2 = converter.binary(numberint2)

                #calls function in converter which converts list value to string value 
                stringa = converter.string(binarynum1)
                stringb = converter.string(binarynum2)
                              
                print ("    ",numberint1, "  = ", stringa)
                print ("    ",numberint2, "  = ", stringb)
                print ("   + ")
                print ("-------------------------------")

                sumlist = adder.adder(binarynum1,binarynum2)#calls adder function

                stringlist = converter.string(sumlist)# convverts binary sum from list to string 

                decimalout = converter.decimal(sumlist)# converts binary sum to decimal sum

                print ("Sum (Binary)  = ", stringlist)
                print ("Sum (Decimal) = ", decimalout)
                print ("---------------------------------------------------------------------------")
                print()
                print()

            else :
                print()
                print("Invalid number.  ")
                print ("Please enter a number in range (0 - 127)")
                print ("---------------------------------------------------------------------------")
                print()
                print()
        else :
            print ()
            print("Invalid number.Do not enter alphabets and other characters. ")
            print ("Please enter a number in range (0 - 127)")
            print ("---------------------------------------------------------------------------")
            print()
            print()
    else :
        print()
        print("Do not leave blank ")
        print ("Please enter a number in range (0 - 127)")
        print ("---------------------------------------------------------------------------")
        print()
        print()
        
        
    an = input ("Do you want to restart the program?(press y to continue)")
    ans = an.lower()
    if ans != "y" :
        print()
        print ("Program has ended.")
        print ("--------------------------------------X-------------------------------------")

    

    
    
