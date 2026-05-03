import json
from pathlib import Path

def print_students(student_list):
    """
    Loops through the student list and prints each student's information.
    """
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )


def main():

    file_path = Path(__file__).parent / "Student.json"

    # Open and load the JSON file into a Python list
    with open(file_path, "r") as file:
        students = json.load(file)

    # Print original student list
    print("This is the original Student list.")
    print_students(students)

    # Add new student to the list
    new_student = {
        "F_Name": "Kobe",
        "L_Name": "Alexander",
        "Student_ID": 212945185,
        "Email": "kalexander@gmail.com"
    }

    students.append(new_student)

    # Print updated student list
    print()
    print("This is the updated Student list.")
    print_students(students)

    # Write updated list back to the JSON file
    with open(file_path, "w") as file:
        json.dump(students, file, indent=4)

    print()
    print("The student.json file was updated.")


if __name__ == "__main__":
    main()