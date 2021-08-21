#!/usr/bin/env python

import re
import json
import argparse

logFiles = []

parser = argparse.ArgumentParser(description="list of log files")
parser.add_argument('file',metavar='file',type=str,help="file that contains the list files")

args = parser.parse_args()
file = args.file

print(file)

# logFiles = ["/mnt/d/Arshad/Freelancing/Websphere/logs/SystemErr.log","/mnt/d/Arshad/Freelancing/Websphere/logs/native_stderr.log"]
logFiles = open(file).read().splitlines()
keyWords = ("hung","error","sql")

print(logFiles)

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
