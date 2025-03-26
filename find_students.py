def find_students(computers_path, physics_path):
    computers = open(computers_path, 'r')
    physics = open(physics_path, 'r')
    
    computers_students = set(line.strip().lower() for line in computers)
    
    mutual_students = []
    for line in physics:
        student = line.strip().lower()
        if student in computers_students:
            mutual_students.append(student)

    computers.close()
    physics.close()
    return mutual_students
    

def main():
    find_students()

if __name__ == "__main__":
    main()
    

        
    


