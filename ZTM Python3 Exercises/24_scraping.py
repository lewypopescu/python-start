import requests
from bs4 import BeautifulSoup
import pprint

headers = {"User-Agent": "Mozilla/5.0"}
urls = [f"https://news.ycombinator.com/news?p={i}" for i in range(1, 3)]

links = []
subtext = []

for url in urls:
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        links.extend(soup.select(".titleline > a"))
        subtext.extend(soup.select(".subtext"))
    else:
        print(f"Failed to fetch {url}")


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda x: x["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select_one(".score")
        if vote:
            points = int(vote.getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))

# Scraping is the process of extracting data from websites. It involves making HTTP requests to web pages, parsing the HTML content, and extracting relevant information. Common libraries for web scraping in Python include BeautifulSoup, Scrapy, and Requests.
