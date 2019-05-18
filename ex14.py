from sys import argv

script, userName = argv
prompt = '> ' #variable to save the script i want before the input

print("Hi %s, i'm the %s script." % (userName, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % userName)
likes = input(prompt)

print ("Where do you live %s." % userName)
lives = input(prompt)

print ("what kind of computer do you have %s." %userName)
computer = input(prompt)

print ("""
so yoy said that %r abouyt liking me.
And you live in %r. Not sure where that is.
and you have a %r computer. Nice.
""" %(likes, lives, computer))