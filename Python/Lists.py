if __name__ == '__main__':  
    N = int(input())  
    l = []  # Initialize an empty list to store the elements
    
    # Loop through each command (based on the number of commands N)
    for i in range(N):
        user = input()  # Read the input command as a string
        user = user.split(" ")  # Split the string into a list of words
        
        # Handle the 'insert' command
        if user[0] == "insert":
            # Insert an element at a specific position in the list
            l.insert(int(user[1]), int(user[2]))
        
        # Handle the 'print' command
        if user[0] == "print":
            # Print the current state of the list
            print(l)
            
        # Handle the 'remove' command
        if user[0] == "remove":
            # Remove the first occurrence of the specified element from the list
            l.remove(int(user[1]))
        
        # Handle the 'append' command
        if user[0] == "append":
            # Add an element to the end of the list
            l.append(int(user[1]))
        
        # Handle the 'sort' command
        if user[0] == "sort":
            # Sort the list in ascending order
            l.sort()
        
        # Handle the 'reverse' command
        if user[0] == "reverse":
            # Reverse the order of the elements in the list
            l.reverse()
            
        # Handle the 'pop' command
        if user[0] == "pop":
            # Remove and return the last element from the list
            l.pop()
