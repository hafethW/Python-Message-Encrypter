import sys

def encode():
    file = sys.argv[2]
    inFile = open(file)
    whole = inFile.read()
    goal = ""
    for char in whole:
        if char.isalpha():
            goal+= chr(ord(char)+500)
        else:
            goal+=char
    outFile = open("encoded.txt","w")
    outFile.write(str(goal))
    outFile.close()
    inFile.close()

def decode():
    file = sys.argv[2]
    inFile = open(file)
    whole = inFile.read()
    goal = ""
    for char in whole:
        if char.isalpha():
            goal+= chr(ord(char)-500)
        else:
            goal+=char
    outFile = open("decoded.txt","w")
    outFile.write(str(goal))
    outFile.close()
    inFile.close()

if sys.argv[1] == "encode":
    encode()
elif sys.argv[1] == "decode":
    decode()
else:
    print(sys.argv[1],"is not a valid command. The only functionalities available are 'encode' and 'decode'" )
