import praw
import sqlite3
import re
import time
import datetime
import praw
from psaw import PushshiftAPI


databaseLocation = "/Users/joshuareid/Documents/GitHub/RedditScraper/venv/src/database.db"
conn = sqlite3.connect(databaseLocation)

reddit = praw.Reddit("bot1")
api = PushshiftAPI(reddit)
subreddit = reddit.subreddit("hardwareswap")


### Uploads data to database
def uploadData(item, price, location, date):
    conn = sqlite3.connect(databaseLocation)
    sqliteStatement = "INSERT INTO posts (Item, price, location, date) VALUES ('{}', '{}', '{}', '{}')"
    cur = conn.cursor()
    cur.execute(sqliteStatement.format(item, price, location, date))
    conn.commit()


### Parses a post for the items, price, location, and date
def parseItem(title, content, date):
    returnData = []
    returnData.append(date)

    # searching for location between the first [ and ]
    m = re.search(r'(?<=\[).+?(?=\])', title)
    if m:
        found = m.group(0)
        returnData.append(found)
    else:
        returnData.append("Location Not Available")



    # searching between [H] and [W] to get items sold
    m = re.search('H](.*?)\[W]', title)
    if m:
        found = m.group(1)
        paypalFound = re.search(" paypal ", found.lower())
        localFound = re.search(" local ", found.lower())
        cashFound = re.search(" cash ", found.lower())
        if paypalFound == None and localFound == None and cashFound == None:
            returnData.append(found)
        else:
            return None


    # searching for $ in post for price
    m = re.findall('(?:[\£\$\€]{1}[,\d]+.?\d*)', content)
    if m:
        found = m.group(0)
        returnData.append(found)
    else:
        returnData.append("Price Not Available")



    if len(returnData) > 1:
        return returnData



### Function created to break down the uploading into months
def uploadAfterSearch(submissionList):
    counter = 1
    print("Starting Upload...")
    for submission in submissionList:
        title = submission.title
        content = submission.selftext
        date = submission.created
        date = datetime.datetime.fromtimestamp(date).date()
        list = parseItem(title, content, str(date))
        if list and len(list) == 4:
            try:
                uploadData(item=list[2], price=list[3], date=list[0], location=list[1])
            except:
                print("Files cannot be added: " + str(counter))
                counter += 1

    print("Upload Complete.")




### Uploading searched posts to database broken down by month just in case program crashes/external error
### Also allows to watch progress.

start_epoch=int(datetime.datetime(2020, 1, 1).timestamp())
end_epoch = int(datetime.datetime(2020, 2, 1).timestamp())

print("Starting January Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             before=end_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("January Search Complete.")
uploadAfterSearch(posts)



start_epoch=int(datetime.datetime(2020, 2, 2).timestamp())
end_epoch = int(datetime.datetime(2020, 3, 1).timestamp())
print("Starting February Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             before=end_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("February Search Complete.")
uploadAfterSearch(posts)


start_epoch=int(datetime.datetime(2020, 3, 2).timestamp())
end_epoch = int(datetime.datetime(2020, 4, 1).timestamp())
print("Starting March Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             before=end_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("March Search Complete.")
uploadAfterSearch(posts)





start_epoch=int(datetime.datetime(2020, 4, 2).timestamp())
end_epoch = int(datetime.datetime(2020, 5, 1).timestamp())
print("Starting April Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             before=end_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("April Search Complete.")
uploadAfterSearch(posts)





start_epoch=int(datetime.datetime(2020, 5, 2).timestamp())
end_epoch = int(datetime.datetime(2020, 6, 1).timestamp())
print("Starting May Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             before=end_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("May Search Complete.")
uploadAfterSearch(posts)




start_epoch=int(datetime.datetime(2020, 6, 2).timestamp())
end_epoch = int(datetime.datetime(2020, 7, 1).timestamp())
print("Starting June Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             before=end_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("June Search Complete.")
uploadAfterSearch(posts)




start_epoch=int(datetime.datetime(2020, 7, 2).timestamp())
end_epoch = int(datetime.datetime(2020, 8, 1).timestamp())
print("Starting July Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             before=end_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("July Search Complete.")
uploadAfterSearch(posts)




start_epoch=int(datetime.datetime(2020, 8, 2).timestamp())
end_epoch = int(datetime.datetime(2020, 9, 1).timestamp())
print("Starting August Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             before=end_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("August Search Complete.")
uploadAfterSearch(posts)



start_epoch=int(datetime.datetime(2020, 9, 2).timestamp())
end_epoch = int(datetime.datetime(2020, 10, 1).timestamp())
print("Starting September Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             before=end_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("September Search Complete.")
uploadAfterSearch(posts)



start_epoch=int(datetime.datetime(2020, 10, 2).timestamp())
end_epoch = int(datetime.datetime(2020, 11, 1).timestamp())
print("Starting October Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             before=end_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("October Search Complete.")
uploadAfterSearch(posts)


start_epoch=int(datetime.datetime(2020, 11, 2).timestamp())
print("Starting November Search...")
posts = list(api.search_submissions(after=start_epoch,
                                             subreddit='hardwareswap',
                                             filter=['created','selftext', 'title', 'subreddit']))

print("November Search Complete.")
uploadAfterSearch(posts)