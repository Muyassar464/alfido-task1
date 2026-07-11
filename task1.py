import os
import shutil
try:
    # 1. Create and write to a text file
    with open("student.txt", "w") as file:
        file.write("Name: Muyassar Ochilova\n")
        file.write("Internship: Alfido Tech\n")
        file.write("Language: Python\n")
    print("File created successfully.")
    # 2. Read the file
    with open("student.txt", "r") as file:
        print("\nReading file:")
        print(file.read())
    # 3. Rename the file
    os.rename("student.txt", "information.txt")
    print("File renamed successfully.")
    # 4. Create a folder
    if not os.path.exists("Backup"):
        os.mkdir("Backup")
    # 5. Move the file
    shutil.move("information.txt", "Backup/information.txt")
    print("File moved successfully.")
    # 6. Delete the file
    os.remove("Backup/information.txt")
    print("File deleted successfully.")
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print("An error occurred:", e)