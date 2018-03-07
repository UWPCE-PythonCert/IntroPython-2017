#!/usr/bin/env python

"""
An Asynchronous version of the script to see how much a given word is
mentioned in the news today

Takes advantage of:

Uses data from the NewsAPI:

https://newsapi.org
"""

import time
import asyncio
import aiohttp
import requests

WORD = "trump"

NEWS_API_KEY = "84d0483394c44f288965d7b366e54a74"

base_url = 'https://newsapi.org/v1/'

# use one session for the whole script
#  recommended by the docs
# session = aiohttp.ClientSession()


# this has to run first, so doesn't really need async
# but why use two reuests libraries ?
async def get_sources(sources):
    """
    get all the english language sources of news

    'https://newsapi.org/v1/sources?language=en'
    """
    url = base_url + "sources"
    params = {"language": "en"}
    session = aiohttp.ClientSession()
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False, params=params) as resp:
            data = await resp.json()
            print("Got the sources")
    sources.extend([src['id'].strip() for src in data['sources']])


async def get_articles(source):
    """
    https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey=1fabc23bb9bc485ca59b3966cbd6ea26
    """
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              # "sortBy": "latest", # some sources don't support latest
              "sortBy": "top",
              # "sortBy": "popular",
              }
    print("requesting:", source)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False, params=params) as resp:
            if resp.status != 200:  # aiohttpp has "status"
                print("something went wrong with: {}".format(source))
                await asyncio.sleep(0)
                return
            data = await resp.json()
            print("got the articles from {}".format(source))
    # the url to the article itself is in data['articles'][i]['url']
    titles.extend([str(art['title']) + str(art['description'])
                   for art in data['articles']])


def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


start = time.time()

# start up a loop:
loop = asyncio.get_event_loop()

# create the objects to hold the data
sources = []
titles = []

# get the sources -- this is essentially synchronous
loop.run_until_complete(get_sources(sources))

# running the loop for the articles
jobs = asyncio.gather(*(get_articles(source) for source in sources))
loop.run_until_complete(jobs)
loop.close()
# session.close()

art_count = len(titles)
word_count = count_word(WORD, titles)

print(WORD, "found {} times in {} articles".format(word_count, art_count))
print("Process took {:.0f} seconds".format(time.time() - start))
