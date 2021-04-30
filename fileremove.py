# importing os module 
import os 
      
# File name 
file = 'file1.txt'
      
# File location 
location = "/Users/rohitmahadik/python-proj/python-proj1"
      
# Path 
path = os.path.join(location, file) 
      
# Remove the file 
# 'file.txt' 
os.remove(path) 

