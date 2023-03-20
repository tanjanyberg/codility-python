def solution(A, K):

    # array A with N integers, K is number of rotations 
    
    N = len(A) 

    if N == 0:
        return []

    for i in range(K):

        j = A[0:N-1] # save all values in A except last
        A[0] = A[N-1] # change first value to last value
        A[1:N] = j # shift all values except last right by one index

    return A
  
  
if __name__ == "__main__":
  
 test = solution([1, 2, 3, 4, 5], 3)
 print(test)
  
    
  
