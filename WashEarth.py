#!/usr/bin/python
import praw
import logging

logging.basicConfig(filename='WashEarthError.log',level=logging.DEBUG)

reddit = praw.Reddit('WashingtonEPBot')
subreddit = reddit.subreddit("EarthPorn")

with open("washingtonKeyWords.txt") as f:
    washington_keywords = f.read().splitlines();
f.close()

for submission in subreddit.stream.submissions():
    normalized_title = submission.title.lower()
    for keyword in washington_keywords:
        try:
            if keyword in normalized_title:
                post_title = str.join('', ('\"', str(submission.title), '\"', ', posted by u/', str(submission.author)))
                reddit.subreddit('WashingtonEarthPorn').submit(url=submission.url, title=post_title)
                break
        except:
            logging.warning("ERROR: ")
            logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.warning('is when this event was logged.')
            logging.warning(normalized_title)
            logging.warning('is what caused the error')
            e = sys.exc_info()[0]
            logging.warning(e)

