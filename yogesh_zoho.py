def pyramid1(n): 

    k = 2*n-1
    num = 1
    for i in range(0, n): 
      
        for j in range(0, k): 
            print(end=" ") 
        k = k - 2
        for j in range(0, i+1):  
            print(num, end=" ") 
            num = num + 1
        print("\r") 
  
n = int(input())
pyramid1(n) 
