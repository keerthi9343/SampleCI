# Define a list of student names and their grades
students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [75, 80, 72]},
    {"name": "Charlie", "grades": [90, 92, 88]},
    {"name": "David", "grades": [65, 70, 60]},
    {"name": "Eva", "grades": [88, 85, 91]}
]

# Function to calculate the average grade for a list of grades
def calculate_average(grades):
    return sum(grades) / len(grades)

# Write the results to a text file
with open(""C:\Users\Keerthishree M\OneDrive\Desktop\student_averages.txt"", "w") as file:
    for student in students:
        average = calculate_average(student["grades"])
        file.write(f"{student['name']}: {average:.2f}\n")
        print(f"{student['name']}: {average:.2f}")

print("Average grades have been written to student_averages.txt.")
