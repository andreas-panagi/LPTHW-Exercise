#PRINTING

formatter = "%r %r %r %r" #variable

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three","four" ))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))

#printing using somekind like arrays
print("{0} {1} {2}".format("array 0","array 1 ", "array 2"))