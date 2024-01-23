import math

def check_status(a, b, flag):
    sign1= int(math.copysign(1,a))
    sign2=int( math.copysign(1,b))  
    if (sign1 != sign2 ) and flag == False:
        print("true")
        return True
    if (sign1 == -1 and sign2 == -1) and flag ==True:
        print("true")
        return True
        print("true")
    else:
        print("false")
        return False
        
check_status(0,0,False)


