# A user enters: " hello WORLD "
# Clean the string by:
# Removing extra spaces
# Converting to lowercase
# Making the first letter uppercase
a=" hello WORLD "
a=a.strip()
a=a.title()
print(a)
# or better version
c = " hello WORLD "
c = c.strip().lower().title()
print(c)
# or 
b = ' hello wrorld '
b = a.strip().replace(' ','_').title()
print(b)