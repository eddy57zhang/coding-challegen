from datetime import datetime, timedelta

def inWindow(str1, str2):
    """check if 2 timestamps are within the 60s window, timestamp str2 is behind str1"""
    month ={'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6, 
            'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12}
    
    y1, month1, d1, h1, m1, s1 = int(str1[-4:]), month[str1[4:7]], int(str1[8:10]), \
                                int(str1[11:13]), int(str1[14:16]), int(str1[17:19])
    y2, month2, d2, h2, m2, s2 = int(str2[-4:]), month[str2[4:7]], int(str2[8:10]), \
                                int(str2[11:13]), int(str2[14:16]), int(str2[17:19])
    t1 = datetime(y1, month1, d1, h1, m1, s1)
    t2 = datetime(y2, month2, d2, h2, m2, s2)
    diff = (t2 - t1).total_seconds()
    if abs(diff) >= 60:
        return False
    else:
        return True
        
def extractHashtag(text):
    """"extract distinct hashtags from a cleaned text and all the hashtags are 
    in lower case
    return a list of distinct hashtags
    """
    tagList = []
    length = len(text)
    i = 0
    while (i < length - 1):
        if text[i] == '#':
            tag = ''
            i += 1
            while (i < length and (text[i].isalnum() or text[i] == '_')):
                tag += text[i].lower()
                i += 1
            #after a hashtag is obtained, add it to the hashtag list    
            if tag not in tagList: #check if the tag is duplicate
                tagList.append(tag)
        else:
            i += 1
    return tagList
    
