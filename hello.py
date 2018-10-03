x = "There are %d people in my family." % 5
sister = "sister"
brother = "brother"
y = "My %s is handsome and my %s is beautiful." % (sister, brother)

print (x)
print (y)

print ("I said: %r."% x)
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)