__author__="Fei Hou"

#Read file
def readFile(path):
    try:
        fileOpen=open(path)
    except:
        print ('File could not be opened:',path)
        exit()
    return fileOpen

#Print each line
def generateLine(fopen):
    for line in fopen:
        yield line

#Split each word
def splitLine(lines):
    lines=lines.rstrip()
    words=lines.split()
    return words