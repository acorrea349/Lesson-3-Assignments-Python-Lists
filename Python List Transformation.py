# Task 1: Given the list of grades:

# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order and print the sorted list.


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort() # This sorts it
grades.reverse() #This will reverse the new sorted list


print(grades)

#Task 2: Calculate the average grade and print it.

average_grades = sum(grades) / len(grades)   # sum(grades): will add all numbers inside grade list. len(grades) will calculate the lenght of grades list to 
                                            # be able to divide the sum of grades by lenght of grades to get the average.

print(average_grades)
