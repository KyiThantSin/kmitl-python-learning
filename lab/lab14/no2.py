def replace_text_in_file():
    filename = input("Enter a filename: ")

    try:
        with open(filename, 'r') as file:
            data = file.read()

        old_string = input("Enter the old string to be replaced: ")
        new_string = input("Enter the new string to replace the old string: ")

        if old_string == new_string:
            print("Old string and new string are the same.")
            return

        data = data.replace(old_string, new_string)

        with open(filename, 'w') as file:
            file.write(data)

        print("Done")

    except FileNotFoundError:
        print("File not found.")

replace_text_in_file()