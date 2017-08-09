from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Does the file extist? {exists(to_file)}")
print("Ready? Press Retrun. Otherwiese, press CTRL+C to abort")
input("?")

with open(to_file, 'w') as f:
    f.write(open(from_file).read())
