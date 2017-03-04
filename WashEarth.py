#!/usr/bin/python
import praw
import logging

reddit = praw.Reddit('WashingtonEPBot')
EPSubreddit = reddit.subreddit("EarthPorn")
WashEPSubreddit = reddit.subreddit("WashingtonEarthPorn")
keywordsFile = "WashingtonKeyWords.txt"

with open(keywordsFile) as f:
    washington_keywords = f.read().splitlines();
f.close()

for submission in EPSubreddit.stream.submissions():
    normalized_title = submission.title.lower()
    for keyword in washington_keywords:
        try:
            if keyword in normalized_title:
                title = str(submission.title)
                user = str(submission.author)
                post_title = str.join('', ('\"', title, '\"', ', posted by u/', user))
                WashEPSubreddit.submit(url=submission.url, title=post_title)
                print("\nPOSTED\n\t" + post_title + "\n")
                break
        except Exception as e:
            print("\nERROR\n\t" + str(submission.title))
            print("\t" + str(e) + "\n")
            break
