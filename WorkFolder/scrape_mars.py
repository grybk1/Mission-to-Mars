from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time


def scrape():
#Scrape News
#first news title
    url ='https://mars.nasa.gov/#news_and_events'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find('h3', class_='title')
    news_title=results.text
    #print(results.a['href'])
    
#  First News Articles Paragraph
    href_path=results.a['href']
    url='https://mars.nasa.gov/'+href_path
    #print(url)
    response = requests.get(url)
    soup2 = BeautifulSoup(response.text, 'lxml')
    #print(soup2)
    results2=soup2.find_all('p')
    # #save to variable
    news_p= results2[3].text

#Featured Image URL
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    marsImage_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mar'
    browser.visit(marsImage_url)

    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    fancy_Button=soup.find('a', class_='button fancybox')  

    #save to variable
    featured_image=fancy_Button['data-fancybox-href']
    featured_image_url='https://www.jpl.nasa.gov'+featured_image
    #print(featured_image_url) 

#Mars Weather Forcast
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
#twitter_url = 'https://twitter.com/marswxreport?lang=en'
    twitter_url='https://twitter.com/MarsWxReport/status/1233751572125028354'
    browser.visit(twitter_url)
    time.sleep(1)
    html=browser.html
    soup = BeautifulSoup(html, 'lxml')
    weather_forcast = soup.find('title')
    mars_weather_forcast=weather_forcast.text


#MARS FACTS
    url='https://space-facts.com/mars/'
    tables=pd.read_html(url)
    tables
    mars_properties_df=pd.DataFrame(tables[0])
    mars_properties_df.columns=['Property','Value']
    planet_compare_df=pd.DataFrame(tables[1])  
    mars_properties_html=mars_properties_df.to_html()
    planet_compare_html=planet_compare_df.to_html()
    mars_properties_html=mars_properties_html.replace('\n', '')
    planet_compare_html=planet_compare_html.replace('\n', '')
    mars_properties_html=mars_properties_html.replace('dataframe', 'table')
    planet_compare_html=planet_compare_html.replace('dataframe', 'table')

    mars_artifacts={}
    mars_artifacts["newsTitle"]=news_title
    mars_artifacts["newsArticle"]=news_p
    mars_artifacts["featuredImage"]=featured_image_url
    mars_artifacts["weatherForcast"]=mars_weather_forcast
    mars_artifacts["propertiesHtml"]=mars_properties_html
    mars_artifacts["earthComparison"]=planet_compare_html
    return mars_artifacts
          
def getHemispheres():
       #MARS HEMISPHERES
    # hemisphere_image_urls=[]
    # hemisphere_image_urls.append({'title':'Valles Marineris Hemisphere' , 'image_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg' })
    # hemisphere_image_urls.append({'title':'Cerberus Hemisphere' , 'image_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg' })
    # hemisphere_image_urls.append({'title':'Schiaparelli Hemisphere' , 'image_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg' })
    # hemisphere_image_urls.append({'title':'Syrtis Major Hemisphere' , 'image_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg' })
    hemisphere_image_urls=[]
    hemisphere_image_urls.append({'title':'Valles Marineris Hemisphere' , 'image_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg' })
    hemisphere_image_urls.append({'title':'Cerberus Hemisphere' , 'image_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg' })
    hemisphere_image_urls.append({'title':'Schiaparelli Hemisphere' , 'image_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg' })
    hemisphere_image_urls.append({'title':'Syrtis Major Hemisphere' , 'image_url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg' })
    
    
    return hemisphere_image_urls           