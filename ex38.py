print("Wait there are not 10 things in tha list. Let's fix it.")

stuffs = ['apple','telephone','strawberry','noodle']
ten_things = "komi gigi carrots water paper cup mail nail cutter pc watch tissue chair table tv"
things = ten_things.split(' ')

while len(stuffs) != 10:
    thing = things.pop()
    stuffs.append(thing)
    print(f"{thing} appended. now length: {len(stuffs)}.")

print("There we go:", stuffs)
print("Let's do something with list")
print(stuffs[0])
print(stuffs[1])
print(stuffs[-1]) # print last item
print(' '.join(stuffs)) # print all items with space delemited
print('#'.join(stuffs[4:6])) # print 4th elements followed by #
