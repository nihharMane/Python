
students = []
grades = []


def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"{name} added with grade {grade}.")


def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        print(f"{name}'s grade updated to {new_grade}.")
    else:
        print(f"{name} not found.")


def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print(f"{name} has been removed.")
    else:
        print(f"{name} not found.")


def average_grade():
    if grades:
        avg = sum(grades) / len(grades)
        print("Average grade of the class:", avg)
    else:
        print("No grades available.")

def highest_and_lowest():
    if grades:
        print("Highest grade:", max(grades))
        print("Lowest grade:", min(grades))
    else:
        print("No grades available.")

add_student("Alice", 85)
add_student("Bob", 92)
add_student("Charlie", 78)

update_grade("Bob", 95)

remove_student("Charlie")

average_grade()

highest_and_lowest()
