#!/usr/bin/python
import praw

reddit = praw.Reddit('WashingtonEPBot')
subreddit = reddit.subreddit("EarthPorn")

with open("washingtonKeyWords.txt") as f:
    washington_keywords = f.read().splitlines();
f.close()

for submission in subreddit.top('all'):
    normalized_title = submission.title.lower()
    for keyword in washington_keywords:
        if keyword in submission.title:
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)
            print("Score: ", submission.score)
            print("---------------------------------\n")
