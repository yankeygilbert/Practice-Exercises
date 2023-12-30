
def solution(sequence):
    modify = 0
    if (sequence[0]>sequence[1]):
        sequence[0]= sequence[1] // 2
        modify += 1
    for i in range(1,len(sequence)):
        if(sequence[i-1]<sequence[i]and sequence[i+1]< sequence[i])or(sequence[i-1]>sequence[i]and sequence[i+1]>sequence[i]):
            sequence[i] = (sequence[i-1]+sequence[i+1])//2
            if(sequence[i]==sequence[i-1]) or(sequence[i]==sequence[i+1]):
                return False
    if(sequence[len(sequence)-1])<(sequence[len(sequence)-2]):
        modify +=1
    if modify >1 :
        return False
    return True
