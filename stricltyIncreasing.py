
def solution(sequence):
    it = 1
    count = 0

    if  len(sequence)==1:
        print("true")
        return True

    nsequence= [i for n,i in enumerate(sequence) if i not in sequence[:n]]
    print(nsequence)

    if (len(sequence)-len(nsequence))>1:
         print("false")
         return False
        
    if (len(sequence)-len(nsequence))==1:
        count += 1

    if  len(nsequence)==1:
        print("true")
        return True


    for a in range (1,len(nsequence)):
        if (a == (len(nsequence)-1)):
             print("true")
             return True
        if nsequence[a]> nsequence[a+1]:
            count += 1
            if count >1:
                print("false")
                return False
        if ((nsequence[a] - nsequence[a-1]) > (nsequence[a]-nsequence[a-1]) and(nsequence[a-1] > nsequence[a+1])) or ((nsequence[a-1] - nsequence[a]) > (nsequence[a]-nsequence[a-1]))  :
            print('false')
            return False

        

solution([40, 50, 60, 10, 20, 30])
