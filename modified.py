def modify_file_content(content):
    """
    Modify the content of the file. 
    For example, convert all text to uppercase.
    """
    return content.upper()
try:
    # Check if the file exists and can be opened
    with open('input.txt', 'w') as file:
        file.write("Hello World!")
        
        # Read the content of the file
        content = file.read()
        print("File content read successfully.")
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: An I/O error occurred while reading the file.")



def main():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read: ")
        
        # Open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_file_content(content)
        
        # Ask the user for the output file name
        output_file = input("Enter the name of the file to write the modified content: ")
        
        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to {output_file}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read or written.")

if __name__ == "__main__":
    main()