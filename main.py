from os import listdir, rename, remove
while True:
    all_files = listdir("files")
    option = int(input("\nMain Menu\n1. New\n2. Edit\n3. Rename\n4. Delete\n5. Exit\nSelect Option: "))
    print()
    if option == 1:
        file_name = input("Enter filename: ")
        if file_name in all_files:
            print("This filename already exists")
            continue
        new_file = open("files/" +  file_name, "w")
        content = input("Enter Content: ")
        new_file.write(content)
        print("File Saved")
        new_file.close()
    elif 1 < option < 5:
        for file in all_files:
            if file != ".readMe.txt":
                print(file)
        if option == 2:
            file_name = input("Enter filename: ")
            if file_name not in all_files:
                print("File not found")
                continue
            file = open("files/" +  file_name, "w")
            content = input("Enter Content: ")
            file.write(content)
            print("File Saved")
            file.close()
        elif option == 3:
            file_name = input("Enter file name to rename: ")
            if file_name not in all_files:
                print("File not found")
                continue
            new_name = input("Enter new name: ")
            rename("files/" + file_name, "files/" + new_name)
            print("File Renamed")
        else:
            file_name = input("Enter file name to delete: ")
            if file_name not in all_files:
                print("File not found")
                continue
            remove("files/" + file_name)
            print("File Deleted")
    elif option == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Option")