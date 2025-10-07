# Read user input for file path
file_path = input("Enter the file path: ").strip()

try:
    # Open the file and read the content
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into words
    words = content.split()

    # Count the number of words
    word_count = len(words)

    print(f"The file contains {word_count} words.")
except FileNotFoundError:
    print("❌ The file was not found. Please check the file path.")
