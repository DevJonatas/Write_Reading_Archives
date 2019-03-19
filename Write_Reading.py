
nameArchive = "archive.txt"

def Write(word):
    archive = open(nameArchive,"w")
    archive.write(word + "{}".format("\n"))
    archive.close()

def AddWord(word):
    archive = open(nameArchive,"a")
    archive.write(word+"{}".format("\n"))
    archive.close()

def Reading():
    archive = open(nameArchive,"r")
    listWords = []
    for words in archive:
        listWords.append(words.strip())
        print(words.strip()) #Mode reading Archive
    archive.close()
    return listWords #Mode List


#AddWord("Okay")
list = Reading()
