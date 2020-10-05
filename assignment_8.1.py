import os

#Make Directory

directory = input("What directory would you like to store your file in?  ") + "/"

try:
	os.mkdir(directory)
except OSError as error:
    print(error)  
 
os.chdir(directory)

#Make File 
filename = input("What is the name of your file?  ");
filename = filename + '.csv'


with open (filename, "w") as f:
	f.write(input("Enter your name, address, and phone number. "));
f.close

print()

with open(filename, "r") as f:
    print(f.read())
f.close    	







    	

