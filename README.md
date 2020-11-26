# Reddit r/HardwareSwap Scraper

## Description
 Script grabs posts from Reddit.com/r/HardwareSwap, parses the posts for needed information, and uploads the data to a SQL Database.
 
<img src="https://github.com/joshuarreid/Reddit-Scraper/blob/main/HardwareSwap.png" />

<br />

## The Problem
A small startup, who was interested in selling computer hardware, needed the market information of used computer hardware. The subreddit r/HardwareSwap is a subreddit that hosts the exchange of unwanted but still useful computer hardware.  They asked me to develop a script to collect all transaction history from the posts of r/hardwareswap.

<br />

## The Script
Post submissions to r/HardwareSwap must follow the title convention of the following:

<img width="500" src="https://github.com/joshuarreid/Reddit-Scraper/blob/main/PostTitle.png" />

The initial brackets include the location, the [H] is what the user is selling, and the [W] is what the user wants. Then within the post content is typically the price of the item. 

My function parseItem() uses regex to find these values and returns an array:



 '''python
    # searching for location between the first [ and ]
    m = re.search(r'(?<=\[).+?(?=\])', title)
    if m:
        found = m.group(0)
        returnData.append(found)
    else:
        returnData.append("Location Not Available")
'''




