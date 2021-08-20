#!/usr/bin/env python

import re
import json
import argparse

logFiles = []

parser1 = argparse.ArgumentParser(description="list of log files")
parser1.add_argument('file',type=str,help="file that contains the list files",required=True)



logFiles = open(file).readlines()

# logFiles = ["D:/Arshad/Freelancing/Hitachi/SystemErr.log","D:/Arshad/Freelancing/Hitachi/native_stderr.log"]
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
                            keywordDictionary[logllEntry] = value

                        except:
                            keywordDictionary[logEntry] = 1

        return (keywordDictionary)



for files in logFiles:
    mainDict[files] = read_file(files)


print (json.dumps(mainDict,indent=4))

# table = PrettyTable(['error name','Occurrences'])



