def solution(seq):
  count = 0
  for i in range(1,len(seq)):
    if i == 1:  
        if seq[i] <= seq[i-1]:
            count += 1
    else:
        try:
            print("rest i =",i)
            if seq[i] <= seq[i-1]:
                count += 1
                if count > 1:    
                    return False
                if (seq[i] <= seq[i-2]) and (seq[i+1] <= seq[i-1]):
                    return False
        except IndexError:
            if (seq[i]<seq[i-1]) and (count > 1):
                return False
            else:
                print("True")
                return True
  print("True")
  return True

solution([3])



