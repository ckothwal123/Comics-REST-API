# All celery tasks are included here
from __future__ import absolute_import, unicode_literals

from celery import shared_task

# from demoapp.models import Widget
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
from typing import List
from webscrape.models import Comics



@shared_task
def scrape_awkward_yeti(pages):

    res = defaultdict(str)

    for page in range(1, pages):
        heading = []
        image_links = []
        url = "https://theawkwardyeti.com/chapter/heart-and-brain/page/" + str(page)
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")
        titles = soup.find_all("h3", "mb-4")
        images = soup.find_all("p", "comic-thumbnail-in-archive")

        for title in titles:
            heading.append(title.text.strip())

        for image in images:
            image_links.append(image.find("img")["src"])

        for title in range(len(heading)):
            res[heading[title]] = image_links[title]

    try:
        for title in res.keys():
            new_record = Comics(
                comic_title=title, comic_type="heart-and-brain", comic_link=res[title]
            )
            new_record.save()
                
        return True

    except:
        return False


@shared_task
def scrape_garfield():
    garfield_comics = defaultdict(str)

    for page_number in range(1, 5):
        url = "http://pt.jikos.cz/garfield/2020/" + str(page_number)
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")
        test_one = soup.find_all("tr")

        for record in test_one:
            garfield_comics[record.find("img")["alt"]] = record.find("img")["src"]

    try:
        for title in garfield_comics.keys():
            new_record = Comics(
                comic_title=title,
                comic_type="garfield",
                comic_link=garfield_comics[title],
            )
            new_record.save()
        return True

    except:
        return False
