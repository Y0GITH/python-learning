# Print all characters in the string:
# "DATA ANALYTICS"
# but skip spaces using continue.
data = "DATA ANALYTICS"
for i in data:
    if i == " ":
        continue
    print(i)