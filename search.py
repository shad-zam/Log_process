
import re
from prettytable import PrettyTable
import json

logFiles = ["D:/Arshad/Freelancing/Hitachi/SystemErr.log","D:/Arshad/Freelancing/Hitachi/native_stderr.log"]
keyWords = ("sunyy","manager","max")

# This invokes the dictionary

keywordDictionary = {}
mainDict = {}

def read_file(logFile):
    with open(logFile) as logFile:
        for eachRow in logFile:

            logSplitList = eachRow.split()
            for i in keyWords:
                for logEntry in logSplitList:
                    if i in logEntry.lower():
                        try:
                            value = keywordDictionary[logEntry]
                            value += 1
                            keywordDictionary[logEntry] = value

                        except:
                            keywordDictionary[logEntry] = 1

        return (keywordDictionary)



for files in logFiles:
    mainDict[files] = read_file(files)


print (json.dumps(mainDict,indent=4))

# table = PrettyTable(['error name','Occurrences'])



