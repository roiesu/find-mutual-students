def find_students2(computers_path, physics_path):
    with open(computers_path) as computers, open(physics_path) as physics:
        line1 = next(computers, None)
        line2 = next(physics, None)
        
        mutual_students = []
        while line1 is not None and line2 is not None:
            computers_student, physics_student = line1.strip().lower(), line2.strip().lower()
            if computers_student == physics_student:
                mutual_students.append(computers_student)
                line1 = next(computers, None)
                line2 = next(physics, None)
            elif computers_student < physics_student:
                line1 = next(computers, None)
            else:
                line2 = next(physics, None)
            
        print(mutual_students)
        return mutual_students

def main():
    find_students2("computers.txt", "physics.txt" )

if __name__ == "__main__":
    main()
        
                 
        
        
    