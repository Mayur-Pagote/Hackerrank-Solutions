if __name__ == '__main__':  
    # Read an integer input from the user and store it in variable 'n'
    n = int(input())  
    
    # Loop through numbers from 1 to 'n' (inclusive)
    for i in range(1, (n + 1)):  
        # Print the current number (i) without a newline at the end (using 'end=""')
        print(i, end="")
