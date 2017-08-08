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

def charToNum(s):
    #takes X or XY input, gives back its number equivalent starting at 0
    #this function is for convenient indexing and it's pretty cool
    if len(s) == 1:
        #for files that went through the weak compressor
        return ord(s)-65
    else:
        #for files that went through the normal compressor
        return (ord(s[0])-65)*26 + ord(s[1])-65

newFileName = filename[:-15] + "_decompressed.txt"
newFile = open(newFileName, 'w')
y = 0

for line in myFile:
    if y == 0:
        keys = line.split(" ")[:-1]
        y = 1
	continue
    words = re.compile("\w+").findall(line)
    for word in words:
        if word.upper() == word:
            while word in line:
                line = line.replace(word, keys[charToNum(word)])
    newFile.write(line)

myFile.close()
newFile.close()

print("Your decompressed file can be found in " + newFileName + ".")
print("Thanks for using Xyphos!")
