def subArraySum(arr, n, s): 
    sum = 0
    start_index = 0
    list_iter = 0
    while list_iter < len(arr): 
        sum = sum + arr[list_iter] 
        while sum > s and start_index < list_iter:
            sum = sum -arr[start_index]
            start_index = start_index + 1
        if sum == s:
            print(start_index+1,list_iter+1)
            return 1
        list_iter += 1  

if __name__ == '__main__':
    element_pair([2,3,4,5,8,9,-1,12],8,17)   
