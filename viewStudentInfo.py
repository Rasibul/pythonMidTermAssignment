def view_student_info(self):
    print(f"Student ID: {self.student_id}")
    print(f"Name: {self.name}")
    print(f"Department: {self.department}")
    print(f"Enrolled: {'Yes' if self.is_enrolled else 'No'}")
