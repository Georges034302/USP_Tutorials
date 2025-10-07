import re

# Read user input for file path and regex pattern
file_path = input("Enter the file path: ").strip()
regex_pattern = input("Enter the regex pattern to match: ").strip()

# Open the file and read the content
with open(file_path, 'r') as file:
    lines = file.readlines()

# Track if any match was found
matches_found = False

# Loop through each line in the file
for line_num, line in enumerate(lines, start=1):
    # Find all matches of the regex pattern in the current line
    matches = re.findall(regex_pattern, line)
    
    if matches:
        matches_found = True
        # Print the matching line
        print(f"Line {line_num}: {line.strip()}")
        for match in matches:
            print(f"  Match: {match}")

if not matches_found:
    print("❌ No matches found.")
