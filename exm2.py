import os

path = "/workspaces/python_practice/demoo.log"

def print_and_count_matching_lines(filepath):

    with open(filepath, "r") as f:
        for line in f:
            if "mi" in line.lower():
                print(line, end="")   # print the matching line
                


filename = os.path.basename(path)
print("File name:", filename)

result = print_and_count_matching_lines(path)
print("\nTotal 'mi' matches:", result)
