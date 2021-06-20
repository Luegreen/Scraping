#!/usr/bin/env python
# coding: utf-8




# Import Splinter and BeautifulSoup and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt
import time 


def scrape_all():
    # Set up Splinter initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    
    news_title, news_paragraph = mars_news(browser)

    #Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": mars_hemispheres(browser),
        "last_modified": dt.datetime.now()
    }
    #stop webdriver and return data 
    browser.quit()
    return data 

def mars_news(browser):

    #Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    #Add try/except for error handling
    try: 
           
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None 

    return news_title, news_p

# ### JPL Space Images Featured Image

def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    #create try/except clause
    try: 
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None 

    # Use the base URL to create an absolute URL
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
    return img_url



#  ## Mars Facts 

def mars_facts():
    #Add try/except for error handling
    try:
        #use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
    except BaseException:
        return None

    #Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    #Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 
# ### Hemispheres
# 

# 1. Use browser to visit the URL 
def mars_hemispheres(browser):
    try:    
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

    except BaseException:
        return None
# 4. Print the list that holds the dictionary of each image url and title.
    hemisphere_image_urls

# 5. Quit the browser
    browser.quit()

if __name__ == "__main__":
    #If running as script, print scraped data
    print(scrape_all())



