import os

students_file = 'student_name.txt'

def add_student(student_inf):
    with open(students_file, 'a', encoding='utf-8') as write_file:
        write_file.write(student_inf + '\n')

def get_all_students():
    if not os.path.exists(students_file):
        return []
    with open(students_file, 'r', encoding='utf-8') as read_file:
        return list(set([line.strip() for line in read_file if line.strip()]))