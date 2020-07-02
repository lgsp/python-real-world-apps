import os


file_path = input("Enter the file path: ")
string_to_modify = input("String to modify: ")
new_string = input("New string: ")

        
for filename in enumerate(os.listdir(file_path)):
    print("File name:", filename)
    new_file_name = filename[1]
    
    for char in new_file_name:
        if string_to_modify in new_file_name:
            position = new_file_name.find(string_to_modify)
            new_file_name = new_file_name[:position] + new_string + new_file_name[position+1:]
            print("New file name:", new_file_name)
            
    if file_path[-1] == '/':
        src = file_path + filename[1]
        dst = file_path + new_file_name
    else:
        src = file_path + '/' + filename[1]
        dst = file_path + '/' + new_file_name
    os.rename(src, dst)
        
