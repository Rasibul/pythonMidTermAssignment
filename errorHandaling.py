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
