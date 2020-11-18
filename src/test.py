import praw
from psaw import PushshiftAPI


r = praw.Reddit("bot1")
api = PushshiftAPI(r)

import datetime as dt

start_epoch=int(dt.datetime(2020, 1, 1).timestamp())

list = list(api.search_submissions(after=start_epoch,
                            subreddit='hardwareswap',
                            filter=['created','selftext', 'title', 'subreddit'],
                            limit=10))

for submission in list:
    title = submission.title
    content = submission.selftext
    date = submission.created


