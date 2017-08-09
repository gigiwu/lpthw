from sys import argv

script, filename = argv

print(f"here is your file: {filename}")

txt = open(filename)
print(txt.read())
