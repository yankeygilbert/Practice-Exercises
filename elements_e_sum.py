def element_pair(arr: list([int]),T)->list([int]):
    i_start,summ,i = 0,0,0
    #loop through array
    while i < len(arr):
        summ += arr[i]
        '''
        if current sum is greater  and current index is greater than 
         start index subtract value at i_start from sum
        '''
        while summ > T  and i > i_start:
            summ -= arr[i_start]
            i_start += 1
        #veirfy to justify just two numbers
        if summ == T:
            if (i-i_start) == 1:
                print(arr[i_start],arr[i])
                return [arr[i_start],arr[i]]
        i += 1
    print(-1)
    return -1

if __name__ == '__main__':
    element_pair([2,8,5,8],7)