# Initialize two empty lists: one to store the results (name and score) and one to store the scores
Result = []  
scorelist = []

if __name__ == '__main__':
    # Read the number of test cases (how many students)
    for _ in range(int(input())):  
        name = input()  # Read the name of the student
        score = float(input())  # Read the score of the student as a float

        # Append the student's name and score as a pair to the 'Result' list
        Result += [[name, score]]
        
        # Append the score to the 'scorelist' (a list of all scores)
        scorelist += [score]

    # Find the second-lowest unique score by:
    # 1. Converting 'scorelist' to a set (to remove duplicates)
    # 2. Sorting the set and selecting the second element (index 1)
    b = sorted(list(set(scorelist)))[1]  

    # Iterate over the 'Result' list and print names of students who have the second-lowest score
    # The 'sorted(Result)' sorts the results lexicographically by name (alphabetically)
    for a, c in sorted(Result):
        if c == b:  # If the score matches the second-lowest score
            print(a)  # Print the student's name
