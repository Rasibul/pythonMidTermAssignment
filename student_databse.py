class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @property
    def department(self):
        return self.__department

    @property
    def is_enrolled(self):
        return self.__is_enrolled

    @is_enrolled.setter
    def is_enrolled(self, value):
        self.__is_enrolled = value

    def drop_student(self):
        self.is_enrolled = False

    def enroll_student(self):
        if not self.is_enrolled:
            self.is_enrolled = True

    def view_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Enrolled: {'Yes' if self.is_enrolled else 'No'}")

class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

def enroll_student_handler(student_list, student_id):
    try:
        student = next((s for s in student_list if s.student_id == student_id), None)
        
        if student is None:
            raise ValueError(f"Error: Invalid student ID. No student found with ID {student_id}.")
        
        if student.is_enrolled:
            raise ValueError(f"Error: Student '{student.name}' is already enrolled.")
            
        student.enroll_student()
        print(f"Success: Student '{student.name}' has been enrolled.")
        
    except ValueError as e:
        print(e)

def drop_student_handler(student_list, student_id):
    try:
        student = next((s for s in student_list if s.student_id == student_id), None)
        
        if student is None:
            raise ValueError(f"Error: Invalid student ID. No student found with ID {student_id}.")
        
        if not student.is_enrolled:
            raise ValueError(f"Error: Student '{student.name}' is not currently enrolled.")
            
        student.drop_student()
        print(f"Success: Student '{student.name}' has been dropped.")
        
    except ValueError as e:
        print(e)

def main_menu():
    # Initialize some student objects
    student1 = Student(student_id=1, name="John Doe", department="Computer Science", is_enrolled=True)
    student2 = Student(student_id=2, name="Jane Smith", department="Business", is_enrolled=True)
    student3 = Student(student_id=3, name="Alice Johnson", department="Engineering", is_enrolled=False)

    StudentDatabase.add_student(student1)
    StudentDatabase.add_student(student2)
    StudentDatabase.add_student(student3)

    while True:
        print("\n--- Student Management System ---")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("\n--- All Students ---")
            for student in StudentDatabase.student_list:
                student.view_student_info()
                print("-" * 20)
        elif choice == '2':
            try:
                student_id = int(input("Enter Student ID to enroll: "))
                enroll_student_handler(StudentDatabase.student_list, student_id)
            except ValueError:
                print("Invalid input! Please enter a valid integer ID.")
        elif choice == '3':
            try:
                student_id = int(input("Enter Student ID to drop: "))
                drop_student_handler(StudentDatabase.student_list, student_id)
            except ValueError:
                print("Invalid input! Please enter a valid integer ID.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
