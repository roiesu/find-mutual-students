def find_students(computers_path, physics_path):
    computers = open(computers_path, 'r')
    physics = open(physics_path, 'r')
    
    computers_students = set(line.strip().lower() for line in computers)
    
    # Created the mutual_Student list for testing, more effiecient (space comlexity) just print common students.
    mutual_students = []
    for line in physics:
        student = line.strip().lower()
        if student in computers_students:
            mutual_students.append(student)

    print(mutual_students)
    
    computers.close()
    physics.close()
    
    return mutual_students
    
def main():
    find_students()

if __name__ == "__main__":
    main()
    

        
    


