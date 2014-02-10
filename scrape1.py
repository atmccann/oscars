'''Scrape wikipedia for nominees from 86th academy awards'''

from bs4 import BeautifulSoup
import requests
import pprint
import csv


#grab first url. tell it to soup. find everything with class "select-box" and write contents to a list
url = "http://en.wikipedia.org/wiki/86th_Academy_Awards"
page = requests.get(url)
soup = BeautifulSoup(page.text)


#categories_list = soup.find_all("th")
#for a in categories_list:
 #   a = soup.find_all('a')
  #  categories.append(a.text)
   # print categories

def get_categories(url):
    categories = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    tables = soup.find_all('table', class_='wikitable') 
    table = tables[0]                                          
    for th in table.find_all('th'):                  
        categories.append(th.text)
    return categories

def get_movies(url):
    movie_titles = []
    tables = soup.find_all("table", class_="wikitable")
    table = tables[0] 
    
    for tr in table.find_all("tr"):                 
        category = []
        for td in tr.find_all("td"):
            for title in td.text.split('\n'):
                if title:
                    category.append(title)
            movie_titles.append(category)
    return movie_titles

movies = get_movies(url)
categories = get_categories(url)
import pprint
import json
category_list = dict(zip(categories, movies))
print(json.dumps(category_list, indent=2))
