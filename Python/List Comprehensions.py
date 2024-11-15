if __name__ == '__main__':
    # Reading inputs: three integers x, y, z, and the target sum n
    x = int(input())  # Input for the maximum value for i
    y = int(input())  # Input for the maximum value for j
    z = int(input())  # Input for the maximum value for k
    n = int(input())  # Input for the target sum of i + j + k
    
    # Initialize an empty list to store valid combinations
    l = []
    
    # Nested loops to iterate over all possible combinations of i, j, k
    # i ranges from 0 to x (inclusive), j ranges from 0 to y (inclusive), 
    # and k ranges from 0 to z (inclusive)
    for i in range(x+1):  # i ranges from 0 to x (inclusive)
        for j in range(y+1):  # j ranges from 0 to y (inclusive)
            for k in range(z+1):  # k ranges from 0 to z (inclusive)
                
                # If the sum of i, j, and k equals n, skip this combination
                if i + j + k == n:
                    continue  # Skip to the next iteration
                
                # Otherwise, add the combination [i, j, k] to the list l
                l.append([i, j, k])
    
    # Print the resulting list of valid combinations
    print(l)
