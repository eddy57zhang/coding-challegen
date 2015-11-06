import sys
import json
fInput = open(sys.argv[1], "r")
fOutput1 = open(sys.argv[2], "w")

unicodeNum = 0
unicodeFlag = False
escapeChar = {
    '"' : '"', 
    "'" : "'",
    "\\" : '\\', 
    '?' : '?',
    "/" : '/',
    "b" : ' ',
    "f" : ' ',
    "a" : ' ',
    "n" : ' ',
    "r" : ' ',
    "t" : ' ',
    "v" : ' '
    }

for line in fInput:
    decodeLine = json.loads(line)
    #timeStamp and text is <type 'unicode'> 
    if 'created_at' in decodeLine:
        timeStamp = decodeLine['created_at']
        text = decodeLine['text']
        """print ("text in string: \n"), text"""
        cleanText = ""
        text = repr(text)
        length = len(text)
        """print ("text in unicode: \n"), text"""
        i = 0
        #go through each character of each text/line
        while (i < length):
            if (text[i] == '\\' and i < length - 1):
                if text[i + 1] in escapeChar:
                    cleanText += escapeChar[text[i + 1]]
                    i += 2
                #utf-8: format : \x[][]
                elif text[i + 1] == 'x' and i < length - 3:
                    i += 4
                    unicodeFlag = True
                #utf-16 format: \u[][][][]
                elif (text[i + 1] == 'u' ) and i < length - 5:
                    i += 6
                    unicodeFlag = True
                #utf-32  format: \U[][][][][][][][]
                elif (text[i + 1] == 'U' ) and i < length - 9:
                    i += 10
                    unicodeFlag = True
                else:
                    cleanText += text[i]
                    i += 1
            else:
                cleanText += text[i]
                i += 1
        #if unicode exist, increase the counter
        if unicodeFlag == True:
            unicodeNum += 1
            unicodeFlag = False
        """print ("after cleaning: \n"), cleanText #, '\n', str(cleanText)""" 
        outputLine = cleanText[2 : -1] + " (timestamp: " + timeStamp +")\n"
        """print ("output line: \n"), outputLine"""
        fOutput1.write(outputLine)
    """print ("--------divding line-----------")"""
"""print ("the # of tweets contain unicode: "), unicodeNum"""
fOutput1.write("\n" + str(unicodeNum) + " tweets contained unicode.")
fInput.close()
fOutput1.close()

