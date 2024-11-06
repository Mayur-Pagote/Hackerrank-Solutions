import math   
import os      
import random  
import re     
import sys    

if __name__ == '__main__':
    # Reading input value and converting it to an integer
    n = int(input().strip())  # The input is expected to be an integer, stripped of extra spaces

    # Check if 'n' is odd
    if n % 2 != 0:
        print("Weird")  # If 'n' is odd, print "Weird"
    
    # Check if 'n' is even and within the range 2 to 5
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")  # If 'n' is even and between 2 and 5 inclusive, print "Not Weird"
    
    # Check if 'n' is even and within the range 6 to 20
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")  # If 'n' is even and between 6 and 20 inclusive, print "Weird"
    
    # Check if 'n' is even and greater than 20
    elif n % 2 == 0 and n > 20:
        print("Not Weird")  # If 'n' is even and greater than 20, print "Not Weird"
