import json
import os
import hashlib

BLOCK_CHAIN_DIRECTORY = os.path.join(os.path.abspath(os.curdir), 'blockchain')

def get_hash(student_folder, filename):
    file_path = os.path.join(BLOCK_CHAIN_DIRECTORY, student_folder, filename)
    with open(file_path, 'rb') as file:
        return hashlib.sha256(file.read()).hexdigest()

def get_files(student_folder):
    folder_path = os.path.join(BLOCK_CHAIN_DIRECTORY, student_folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return [f for f in os.listdir(folder_path) if f.isdigit()]

def sort_files(student_folder):
    files = get_files(student_folder)
    number_of_file = sorted([int(i) for i in files])
    if number_of_file:
        last_file = number_of_file[-1]
        filename = str(last_file + 1)
        return last_file, filename
    return 0, '1'

def block_check(student_folder):
    files = get_files(student_folder)
    number_of_file = sorted([int(i) for i in files])
    result = []

    for elem in number_of_file[1:]:
        with open(os.path.join(BLOCK_CHAIN_DIRECTORY, student_folder, str(elem)), 'r', encoding='utf-8') as f:
            hsh = json.load(f)['Hash']
        
        last_file = str(elem - 1)
        actual_hash = get_hash(student_folder, last_file)

        res = 'All is good' if actual_hash == hsh else 'Changed'
        result.append({'Block': last_file, 'Result': res})

    return result

def write_block(f_and_s_name, lesson, mark, date, prev_hash=''):
    f_and_s_name = f_and_s_name.upper()
    student_folder = os.path.join(BLOCK_CHAIN_DIRECTORY, f_and_s_name)
    
    if not os.path.exists(student_folder):
        os.makedirs(student_folder)
    
    last_file, filename = sort_files(f_and_s_name)
    
    if last_file > 0:
        prev_hash = get_hash(f_and_s_name, str(last_file))

    data = {
        'Last Name, First Name': f_and_s_name,
        'Lesson': lesson,
        'Grade': mark,
        'Date': date,
        'Hash': prev_hash
    }

    with open(os.path.join(student_folder, filename), 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return f"Block {filename} has been added to the blockchain for {f_and_s_name}"