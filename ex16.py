from sys import argv

script, filename = argv

print(f"we are going to clear this file: {filename}\nIf you don't want so, press CTRL+C. otherwise, RETURN")
input("?")

target = open(filename,mode='w')

print("empty file")
target.truncate()

print("now, give me 2 lines")
line1 = input("line 1:")
line2 = input("line 2:")

print(f"i'll write these lines into {filename}")
target.write(line1+"\n"+line2)

print("finally, close the file")
target.close()
