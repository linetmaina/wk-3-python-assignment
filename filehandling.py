def read_and_modify_file(input_file, output_file):
    """
    Reads content from input_file, modifies it, and writes to output_file.
    Modification: converts text to uppercase.
    """
    try:
        with open(input_file, "r") as infile:
            content = infile.read()

        modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_file}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read/write the file.")


if __name__ == "__main__":
    # Ask user for the filename
    input_filename = input("Enter the name of the file to read: ").strip()
    output_filename = "modified_" + input_filename

    read_and_modify_file(input_filename, output_filename)
