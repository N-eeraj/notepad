from os import listdir
while True:
    all_files = listdir("files")
    option = int(input("\nMain Menu\n1. New\n2. Edit\n3. Rename\n4. Delete\n5. Exit\nSelect Option: "))
    if option == 1:
        file_name = "files/" +  input("Enter filename: ") + ".txt"
        if file_name[6:] in all_files:
            print("This filename already exists")
            continue
        new_file = open(file_name, "w")
        content = input("Enter Content: ")
        new_file.write(content)
        print("File Saved")
        new_file.close()
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Option")