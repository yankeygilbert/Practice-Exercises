def element_pair(arr: list([int]),T)->list([int]):
    i_start,summ,i = 0,0,0
    while i < len(arr):
        summ += arr[i]
        while summ > T  and i > i_start:
            summ -= arr[i_start]
            i_start += 1
        if summ == T:
            if (i-i_start) == 1:
                print(arr[i_start],arr[i])
                return [arr[i_start],arr[i]]
        i += 1
    print(-1)
    return -1

if __name__ == '__main__':
    element_pair([2,3,4,5,8,9,-1,12],17)