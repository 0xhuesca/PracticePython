'''
https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on 
the New York Times homepage.

'''

import requests
from bs4 import BeautifulSoup


url="https://www.nytimes.com"
r=requests.get(url)
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())









