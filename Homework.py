def find_students():
    computers = open("computers.txt", 'r')
    physics = open("physics.txt", 'r')
    
    computers_students = set(line.strip().lower() for line in computers)
    physics_students = set(line.strip().lower() for line in physics)
    
    for student in computers_students:
        if student in physics_students:
            print(student)

    computers.close()
    physics.close()

def main():
    find_students()

if __name__ == "__main__":
    main()
    
        
    


