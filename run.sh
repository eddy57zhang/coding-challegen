#The first feature: clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.
python ./src/cleanTweets.py ./tweet_input/input2.txt ./tweet_output/ft1.txt
#The second feature: calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.
python ./src/averageDegree.py ./tweet_input/input2.txt ./tweet_output/ft2.txt
