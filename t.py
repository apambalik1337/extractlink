import re
import os

print("Example: /home/apambalik/Desktop/text.txt")
file_path = input("Please enter the path of the input text file (.txt): ").strip('\"')

with open(file_path, "r") as file:
    contents = file.read()

links = re.findall(r'(https?://\S+)', contents)

if len(links) > 0:
    print("\033[92mLinks found in the input file:\033[0m")
    for link in links:
        print(link)
    output_file = os.path.splitext(file_path)[0] + "_result.txt"
    with open(output_file, "w") as file:
        file.write("Links found in the input file:\n")
        for link in links:
            file.write(link + "\n")
            
        print("Output (result) saved to:", output_file)
else:
    print("No links found in the input file.")