#STRING AND TEXT

x = "There are %d types of people" %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" %(binary, do_not)

print (x)
print (y)

print ("i said: %r." %x)
print ("i also said: '%r'." %y)

hilarious = False
JokeEvaluation = "Isn't that joke so funny?! %r"

print (JokeEvaluation %hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)

