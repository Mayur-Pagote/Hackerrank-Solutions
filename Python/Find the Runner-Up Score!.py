# Read an integer n from the input (though it's not actually used in the logic below)
n = int(input())

# Read a list of integers from the input and store them in the variable arr
arr = list(map(int, input().split()))

# Initialize variable x to -100, which is assumed to be a value lower than any element in the array
# and initialize y to the maximum value from the array, arr
x = -100
y = max(arr)

# Iterate through each element in the array
for i in arr:
    # Check if the current element i is greater than x and less than y (i.e., between x and y)
    if i > x and i < y:
        # If the condition is true, update x to the current element i
        x = i
    else:
        # If the condition is false, continue to the next element (this line is unnecessary)
        continue

# Print the value of x after the loop ends
print(x)
