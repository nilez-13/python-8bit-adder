
def check(numberlist):
    conformation=""
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in range( len(numberlist)):
        singleval= numberlist[i]
        ans = singleval in num
        if ans ==False:
            conformation = "not"
            break 
        else :
            conformation = "ok"

    return conformation

def null(number):
    conformation=""
    if number and not number.isspace():
        conformation = "ok"
    else :
        conformation = "not ok "

    return conformation


