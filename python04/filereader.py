#!/usr/bin/env python3
import sys

# Append lines from STDIN to a file
def append_file(filename):
    print(f"Appending to {filename}. Enter text (type 'q' to stop):")
    with open(filename, "a", encoding="utf-8") as f:
        while True:
            line = input()
            if line.lower() == "q":
                break
            f.write(line + "\n")
    print(f"✅ Data saved to {filename}")

# Show file content
def show_content(filename):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())

# Count words in file
def word_count(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return len(text.split())

# Main program
def run():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python fileops.py -a <file>   # append/create file")
        print("  python fileops.py -s <file>   # show file content")
        print("  python fileops.py -c <file>   # show word count")
        sys.exit(1)

    op = sys.argv[1]
    filename = sys.argv[2]

    match op:
        case "-a":
            append_file(filename)
        case "-s":
            show_content(filename)
        case "-c":
            print(f"Word count = {word_count(filename)}")
        case _:
            print("❌ Invalid argument! Use -a, -s, or -c.")

if __name__ == "__main__":
    run()
