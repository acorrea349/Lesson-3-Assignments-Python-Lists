# Problem Statement: You have two lists of student names. One list contains the names of students who have submitted their assignments,
# and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? 
# And how can you check to see if Alice is in both submitted and attended in one if statement?

print("Alice" in submitted) # Alice submitted assignment = True
print("Alice" in attended) # Alice attended class = True
print("Alice" in submitted and "Alice" in attended) # Alice attended and submitted in one statement = True



