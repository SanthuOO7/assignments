def game_with_number (arr,  n) : 
    #Complete the function
    output = []
    for i in range(n-1):
        arr[i]=arr[i] | arr[i+1]
        output.append(arr[i])
        
    output.append(arr[i+1])
    return (output)