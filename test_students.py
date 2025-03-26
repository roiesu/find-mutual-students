from find_students import find_students

def test_find_mutual(tmp_path):
    computers = tmp_path / "computers.txt"
    physics = tmp_path / "physics.txt"
    
    computers.write_text("Adi Sudakevitz\nRoie Sudakevitz\n")
    physics.write_text("Roie Sudakevitz\nOren Bachar\n")
    
    result = find_students(str(computers), str(physics))
    expected = ["roie sudakevitz"]
    assert sorted(result) == sorted(expected)

def test_empty_files(tmp_path):
    computers = tmp_path / "computers.txt"
    physics = tmp_path / "physics.txt"
    
    computers.write_text("")
    physics.write_text("")
    
    result = find_students(str(computers), str(physics))
    expected = []
    assert sorted(result) == sorted(expected)
    
def test_no_mutual(tmp_path):
    computers = tmp_path / "computers.txt"
    physics = tmp_path / "physics.txt"
    
    computers.write_text("Adi Sudakevitz\n")
    physics.write_text("Roie Sudakevitz\n")
    
    result = find_students(str(computers), str(physics))
    expected = []
    assert sorted(result) == sorted(expected)
    
def test_case_insensitive(tmp_path):
    computers = tmp_path / "computers.txt"
    physics = tmp_path / "physics.txt"
    
    computers.write_text("roie Sudakevitz\n")
    physics.write_text("Roie Sudakevitz\n")
    
    result = find_students(str(computers), str(physics))
    expected = ["roie sudakevitz"]
    assert sorted(result) == sorted(expected)
    
def test_large_files(tmp_path):
    computers = tmp_path / "computers.txt"
    physics = tmp_path / "physics.txt"
    
    common_students = [f"student{i}" for i in range(1000, 1050)]
    only_computers = [f"computers{i}" for i in range(5000)]
    only_physics = [f"physics{i}" for i in range(5000)]

    comp_list = only_computers + common_students
    phys_list = only_physics + common_students

    computers.write_text("\n".join(comp_list))
    physics.write_text("\n".join(phys_list))

    result = find_students(str(computers), str(physics))
    expected = [name for name in common_students]
    assert sorted(result) == sorted(expected)


    
    
    
    