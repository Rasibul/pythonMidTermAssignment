from studentClass import Student
from studentDatbase import StudentDatabase


student1 = Student(student_id=1, name="John Doe", department="Computer Science", is_enrolled=True)
student2 = Student(student_id=2, name="Jane Smith", department="Business", is_enrolled=True)
student3 = Student(student_id=3, name="Alice Johnson", department="Engineering", is_enrolled=False)


StudentDatabase.add_student(student1)
StudentDatabase.add_student(student2)
StudentDatabase.add_student(student3)


print(f"Successfully added {len(StudentDatabase.student_list)} students to the database.")
