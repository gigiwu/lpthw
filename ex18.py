def print_two(*args):
    argv1, argv2 = args
    print(f"argv1: {argv1}, argv2: {argv2}")

def print_two_again(argv1, argv2):
    print(f"argv1: {argv1}, argv2: {argv2}")

def print_one(argv1):
    print(f"argv1: {argv1}")

def print_none():
    print(f"nothing")

print_two("gigi", "kimo")
print_two_again("gigi","komi")
print_one("gigi")
print_none()
