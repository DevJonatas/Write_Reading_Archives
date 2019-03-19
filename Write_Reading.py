

def Write(word):
    archive = open("archive.txt","w")
    archive.write(word + "{}".format("\n"))
    archive.close()

def AddWord(word):
    archive = open("archive.txt","a")
    archive.write(word+"{}".format("\n"))
    archive.close()

def Reading():
    archive = open("archive.txt","r")
    listWords = []
    for words in archive:
        listWords.append(words.strip())
        print(words.strip()) #Mode reading Archive
    archive.close()
    return listWords #Mode List


#AddWord("Okay")
list = Reading()
