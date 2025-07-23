import subprocess                           #subprocess is a python module to run the linux commands using python script.

#subprocess.run('ls -lrt', shell=True)      #This linux cmd will execute in the current location where this file is present.

subprocess.run('touch new-file', shell=True)    #To create a new file named "new-file"

subprocess.run('echo "Hello Srikanth" > new-file',shell=True)   #To write content to the new file.

result = subprocess.run('hostname',shell=True, stdout=subprocess.PIPE)  #This is to print the output of 'hostname' on the terminal.

print(result)          #Printing the 'hostname' output stored in variable 'result'.