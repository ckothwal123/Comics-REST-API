# All celery tasks are included here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
# from demoapp.models import Widget
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
from typing import List
from webscrape.models import HeartAndBrain

@shared_task
def add(x, y):
    print("Process started from celery")
    return x + y

@shared_task
def scrape_awkward_yeti(pages):
    
    res = defaultdict(str)

    for page in range(1,pages):
        heading = []
        image_links = []
        url = "http://theawkwardyeti.com/chapter/heart-and-brain-2/page/"+str(page)
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        titles = soup.find_all("h2","post-title")
        images = soup.find_all("p", "comic-thumbnail-in-archive")

        for title in titles:
            heading.append(title.text)
            
        for image in images:
            image_links.append(image.find("img")["src"])
        
        for title in range(len(heading)):
            res[heading[title]] = image_links[title]

    
    for title in res.keys():
        new_record = HeartAndBrain(heading = title, src_link = res[title])
        new_record.save()
    
    return res

@shared_task
def s3_bucket_upload(comic_name, bucket_name):
    pass

