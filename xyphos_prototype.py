import operator
import re
#stackexchange pointed me to these libraries. should be useful

print("Welcome to Xyphos, a text file compressor made by Kyle Franke.")

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
        #does not conserve case. i might end up changing that
        word = word.lower()
        if word not in redundancies.keys():
            redundancies[word] = 1
        else:
            redundancies[word] += 1

#need to sort redundancies, take the 60 most used words
tupleList = sorted(redundancies.items(), key=operator.itemgetter(1))
tupleList.reverse()
tupleList = tupleList[:60]
#ascii int value for 'A'
z = 65
for a in range(len(tupleList)):
    rep = chr(z)
    compression[tupleList[a][0]] = rep
    if z == 122:
        break
    z += 1

newFilename = filename[:len(filename)-4] + "_compressed.txt"
compFile = open(newFilename, 'w')

#to be continued... assign key-value pairings and compressed text to
#<file>_compressed.txt, line by line. looking into efficient solutions
