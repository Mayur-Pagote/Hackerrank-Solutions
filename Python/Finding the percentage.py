if __name__ == '__main__':
    
    # Read the number of students (n) from input.
    n = int(input())
    
    # Initialize an empty dictionary to store student names and their corresponding scores.
    student_marks = {}
    
    # Loop through the number of students (n) to read their data.
    for _ in range(n):
        # Read the student's name and their scores (using *line to capture multiple scores).
        name, *line = input().split()
        
        # Convert the scores from string to float and store them in a list.
        scores = list(map(float, line))
        
        # Add the student's name and their scores to the dictionary.
        student_marks[name] = scores
    
    # Read the name of the student for whom the average score is to be calculated.
    query_name = input()
    
    # Calculate the average score of the queried student by summing their scores and dividing by 3.
    # (Assumes there are always 3 scores per student.)
    average_marks = (sum(student_marks[query_name])/3)
    
    # Print the average score, formatted to 2 decimal places.
    print("{:.2f}".format(average_marks))
