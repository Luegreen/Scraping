#!/usr/bin/env python
# coding: utf-8
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import time

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()


# ### Featured Images
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)

df.to_html()

browser.quit()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 
# ### Hemispheres
# 

# 1. Use browser to visit the URL 

url1 = 'https://marshemispheres.com/'
browser.visit(url1)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for i in range(0,4):
    hemispheres = {}
    try:
        browser.find_by_css('a.product-item img')[i].click()
        title=browser.find_by_css('h2.title')
        #print(title.text)
        time.sleep(2)
        imgs = browser.find_by_text('Sample')
        #print(imgs['href'])
        time.sleep(2)
        hemispheres["title"]=title.text
        hemispheres["imgs"]=imgs['href']
        hemisphere_image_urls.append(hemispheres)
        print(hemispheres)
        browser.back()
    except Exception as e:
        print(e)

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()

