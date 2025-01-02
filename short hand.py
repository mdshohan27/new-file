try:
    with open("file.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("the file was not found!")
else:
    print("File read successfully")
finally:
    print("Operation complete")