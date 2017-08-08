from sys import argv

script, user_name = argv
promt = '>'

print(f"Hi {user_name}! Do you like me?")
like = input(promt)

print(f"""
ok, {user_name}
you said {like} about liking me.
""")
