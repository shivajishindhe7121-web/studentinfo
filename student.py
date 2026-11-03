import sys
course1 = sys.argv[1]
marks1 = int(sys.argv[2])

course2 = sys.argv[3]
marks2 = int(sys.argv[4])

course3 = sys.argv[5]
marks3 = int(sys.argv[6])

total = marks1 + marks2 + marks3
average = total / 3
largest = max(marks1, marks2, marks3)
smallest = min(marks1, marks2, marks3)

print("\n--- Student Marks Report ---")
print(course1, ":", marks1)
print(course2, ":", marks2)
print(course3, ":", marks3)
print("Total Marks:", total)
print("Average Marks:", average)
print("Largest Marks:", largest)
print("Smallest Marks:", smallest)