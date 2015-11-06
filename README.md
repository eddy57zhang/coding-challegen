# coding-challegen
insight coding challenge

All the codes are written and tested under Python 2.7.

The 'src' folder contains 3 source code files:
‘cleanTweets.py’ takes the JSON messages obtained by Twitter Streaming API as input. It removes the non-Ascii Unicode, keeps the printable Ascii characters and replaces escape characters with their counterparts. The json module is used.
‘averagDegree.py’ takes the JSON messages obtained by Twitter Streaming API as input. It first cleans the tweet text using the same method in cleanTweets.py and then calculates the average degree of graphs obtained by using the hashtags of tweets that are in the 60s window as the vertices.
‘functions.py’ contains 2 functions used in averagDegree.py and requires module 'datetime'. The first function ‘inWindow’ takes 2 timestamps obtained from the JSON message as input and returns if the 2 timestamps are within the 60 seconds (exclusive) window. The second function ‘extractHashtag’ extracts hashtags from the cleaned tweet text.

The 'tweet_input' folder contains the tweets obtained from Twitter Streaming API: tweets.txt

The 'tweet_output' folder contains the following 2 output file:
‘ft1.txt’ contains the cleaned tweet text and shows the number of tweets which contain the non-Ascii Unicode
‘ft2.txt’ contains rolling average degree of the hashtag graph.

‘run.sh’ contains 2 shell scripts that are able to compile and run the 2 source code files independently.

