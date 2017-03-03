#!/usr/bin/python
import praw
import logging

#logging.basicConfig(filename='WashEarthError.log',level=logging.DEBUG)

reddit = praw.Reddit('WashingtonEPBot')
subreddit = reddit.subreddit("EarthPorn")

with open("WashingtonKeyWords.txt") as f:
    washington_keywords = f.read().splitlines();
f.close()

for submission in subreddit.stream.submissions():
    normalized_title = submission.title.lower()
    #print(normalized_title)
    for keyword in washington_keywords:
        try:
            if keyword in normalized_title:
                post_title = str.join('', ('\"', str(submission.title), '\"', ', posted by u/', str(submission.author)))
		print('Found ' + keyword + ' in ' + normalized_title)
		reddit.subreddit('WashingtonEarthPorn').submit(url=submission.url, title=post_title)
                break
        except Exception as e:
            print("ERROR")
            print(submission.title)
            print(e)
            break
