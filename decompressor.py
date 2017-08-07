import operator
import re
#stackexchange pointed me to these libraries. should be useful

print("Welcome to Xyphos, a text file compressor made by Kyle Franke.")
print("You are currently using the decompression module. This requires\n" +\
        "a valid compressed text file input, so if you haven't used the\n" +\
        "compression module yet, check out compressor.py before using this.\n")
#even more user input shenanigans
x = True
while x:
    try:
	filename = raw_input("Please type the name of the text file to " +\
                "decompress: ")
	while filename[len(filename)-15:] != "_compressed.txt":
        	filename = raw_input("Invalid file type. Must be a compressed" +\
                        " text file (_compressed.txt).\nPlease try again: ")
        myFile = open(filename, 'r')
    except:
	print("File not found.")
    else:
        x = False

#anyone who makes fun of me for loving python can get bopped!
#look at this line of code it's beautiful
keys = myFile.readline().split(" ")[:-1]
#damn. that's good stuff. anyway, let's move on

def charToNum(s):
    #takes X input, gives back its number equivalent starting at 0
    #this function is for convenient indexing and it's pretty cool
    #this can be easily changed to account for XY input, so I'm keeping it
    return ord(s)-65

for line in myFile:
    #TO DO:
    # -go through file and replace chars with appropriate keys
