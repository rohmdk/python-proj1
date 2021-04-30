greeting = "Good morning, "
user = "Rohit"
total = greeting + user
total = str(total)
print(total)
print(type(total))



import os
stream = os.popen('ls -la')
output = stream.readlines()