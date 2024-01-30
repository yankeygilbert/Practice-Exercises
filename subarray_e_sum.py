def subArraySum(arr,s): 
    sum,start_index,list_iter  = 0,0,0
    
    while list_iter < len(arr): 
        sum = sum + arr[list_iter] 
        while sum > s and start_index < list_iter:
            sum = sum -arr[start_index]
            start_index = start_index + 1
        if sum == s:
            print(start_index+1,list_iter+1)
            return 1
        list_iter += 1  
    print('-1')
    

if __name__ == '__main__':
    subArraySum([1,2,3,5,5],7)   
