from sys import argv

script, filename = argv



def print_all(f):
    print(f.read())

def print_one_line(current_line, f):
    print(current_line, f.readline())

def rewind(f):
    f.seek(0)

in_file = open(filename)

print("print whole file")
print_all(in_file)

print("rewind")
rewind(in_file)

line = 1
print_one_line(line, in_file)

print_one_line(line+1, in_file)
