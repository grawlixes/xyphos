import operator
import re
#stackexchange pointed me to these libraries. should be useful

print("Welcome to Xyphos, a text file compressor made by Kyle Franke.")
print("You are currently using the compression module. If you want to\n" +\
	"decompress a file, select decompression.py.")
print("This is for smaller files. Use the compressor for files >150KB.")

#user input shenanigans
x = True
while x:
    try:
	filename = raw_input("Please type the name of the text file to " +\
                "compress: ")
	while filename[len(filename)-4:] != ".txt":
        	filename = raw_input("Invalid file type. Must be .txt. " +\
			"Please try again: ")
        myFile = open(filename, 'r')
    except:
	print("File not found.")
    else:
        x = False

redundancies = {}
compression = {}

for line in myFile:
    if len(line.strip()) == 0:
        continue
    #well that's convenient
    words = re.compile("\w+").findall(line)
    for word in words:
        if len(word)==1 or len(word)==2:
            continue
        #does not conserve case. oops
        word = word.lower()
        if word not in redundancies.keys():
            redundancies[word] = 1
        else:
            redundancies[word] += 1

#need to sort redundancies, take the 60 most used words
tupleList = sorted(redundancies.items(), key=operator.itemgetter(1))
tupleList.reverse()
wordList = []
#take the 60 most used words
for el in tupleList[:60]:
    wordList.append(el[0])

#ascii int value for 'A'
z = 65
for element in wordList:
    compression[element] = chr(z)
    if z == 90:
        break
    z += 1

newFilename = filename[:len(filename)-4] + "_compressed.txt"
compFile = open(newFilename, 'w')

myFile.close()

myNewFile = open(filename, 'r')

for comKey in compression:
    compFile.write(comKey + " ")

compFile.write("\n")

for line in myNewFile:
    newline = line.lower()
    words = re.compile("\w+").findall(newline)
    for word in words:
        if len(word)==1 or len(word)==2:
            continue
        word = word.lower()
        if word in compression.keys():
            newline = newline.replace(word, compression[word])
    compFile.write(newline)

compFile.close()

print("Compressed file can be found in " + newFilename + ".")
