# In the string: "email: user123@gmail.com"
# Use string methods to extract the username part before @.
email =  "user123@gmail.com"
a= email.find("@")
print(f"{email[:a]}")
