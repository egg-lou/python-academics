students = [["BSIT", ["David", "Alenere"]], ["BSCS", ["Jaymar", "Emman", "Patrick"]]]


def display_students(course_students):
    for course in course_students:
        print(course[0])
        for student in course[1]:
            print(f"   - {student}")


display_students(students)
