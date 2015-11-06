import sys
import json
from functions import inWindow, extractHashtag

fInput = open(sys.argv[1], "r")
fOutput2 = open(sys.argv[2],"w")

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
"""
timeTrain stores the timestamps of each tweet. It keeps updating with new tweetw coming in
such that it only contains the timestamps within 60s window
"""
timeTrain = []
"""
Each element of verList stores the hashtags(a list) extracted from a tweet. It keeps updating
such that it only contains the hashtags extracted from tweets within 60s window
"""
verList = []
"""
graph stores the graph formed by the hashtags and keeps updating such that it only contains 
the hashtags extracted from tweets within 60s window. graph is a dictionary. The key is a 
vertex of the graph and the value is the list containing the vertices it connects with. There 
maybe duplicate vertex in the list since the same edge may appears multiple times within the 
60s window. But this will be taken care of when calculating the averge degree of the graph, by 
using set(). In this way, multiple edges between 2 vertices are only counted once when calculating 
the vertex degree.
"""
graph = {}

for line in fInput:
    decodeLine = json.loads(line)
    #timeStamp and text is <type 'unicode'> 
    if 'created_at' in decodeLine:
        timeStamp = decodeLine['created_at']
        text = decodeLine['text']
        cleanText = ""
        text = repr(text)
        length = len(text)
        i = 0
        #first clean tweet text in the while loop
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
                
        #add the new timestamp
        timeTrain.append(timeStamp)
        #extract hashtag/vertices from cleanText
        hashtag = extractHashtag(cleanText)
        """print "hashtags:", hashtag"""
        #add the new vertex list
        verList.append(hashtag)    
       
        tweetNum = len(timeTrain) 
        delLineNum = []
        #remove edges if the timestamp is out of 60s window from now
        #we do the removal from the oldest tweet
        for j in range(0, tweetNum - 1):
            # if in the window, no need to consider the tweets from the one with the
            #  time stamp 'stamp' to newly added tweet, sicne tweets come in in order  
            if (inWindow(timeTrain[j], timeTrain[-1]) == True): 
                break
            #out of the window, remove edges, update graph
            else: 
                #record the line # that need to be deleted
                delLineNum.append(j)
                #update the vertices and degree for removing the edges/vertices 
                #those are outside the window from the graph'''
                """print "vertex list:" , verList[j]
                print "graph before delet: \n", graph"""
                if len(verList[j]) > 1:
                    for m in range(0, len(verList[j])): #vertices in j-th tweet
                        #all the other verteices execept vreList[j][m]
                        temp1 = verList[j][: m] + verList[j][(m + 1) :]
                        for each in temp1:
                            graph[verList[j][m]].remove(each)
                        #if the vertex degree is 0, delete it
                        if len(graph[verList[j][m]]) == 0:
                            del graph[verList[j][m]]
                        """print graph"""
        #delete the timestamp and the vertex list that are out of the window
        if len(delLineNum) > 0:
            timeTrain[delLineNum[0] : delLineNum[-1] + 1] = []
            verList[delLineNum[0] : delLineNum[-1] + 1] = []
            
        #update the vertices and degree after adding the new edges/vertices into the graph
        vertexNum = len(hashtag)
        if vertexNum > 1 :
            for k in range(0, vertexNum):               
                temp = hashtag[: k] + hashtag[(k + 1) :]
                if hashtag[k] in graph:
                    #a vertex may connect another vertex multiple times
                    graph[hashtag[k]].extend(temp)
                else:
                    graph[hashtag[k]] = temp
    
        """
        print "one loop afte: \n", graph
        print "---------------dividing line------------------------"
        """
        #calculate average degree
        if len(graph) == 0:
            avgDegree = 0
        else:
            lenSum = 0
            for x in graph:
                #using set() make sure multiple edges between 2 vertices are counted as 1
                lenSum += len(set(graph[x]))
            avgDegree = 1.0*lenSum/len(graph)
        fOutput2.write("%0.2f" % avgDegree + '\n')

fInput.close()
fOutput2.close()
