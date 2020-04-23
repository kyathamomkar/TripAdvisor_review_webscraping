# importing the libraries
from bs4 import BeautifulSoup
import requests
import parser
import csv
import os
import json
from urllib import request


global str
reviewer_name =""
review_date= ""
location =""
name=""
date=""
gender=""
url=""
# Step 3: Analyze the HTML tag, where your content lives
# Create a data dictionary to store the data.



def my_function(soup):
  with open('purificadora.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    
       # print(location)
    for main_frame in soup.find_all("div", attrs={"class": "hotels-community-tab-common-Card__section--4r93H"}):
      
      for each in main_frame.find_all("div", attrs={"class": "social-member-event-MemberEventOnObjectBlock__event_wrap--1YkeG"}):
        for div in each.find_all("div", attrs={"class": "social-member-event-MemberEventOnObjectBlock__event_type--3njyv"}):
          review_date = div.text
          location ="Mexico"
        for location in each.find_all("span", attrs={"class": "social-member-common-MemberHometown__hometown--3kM9S"}):
          location = location.text
        s= review_date.split(" escribió una opinión (")
       # s= review_date.split(" wrote a review ")
        name=s[0]
        date=s[1]
        #realdate=s[1]
        realdate=date.replace(")","")
        
        date=date.replace(")","")
        date2 = date.split(" ")
        print(date2[2])
        if(int(date2[2])<2019):
          break
        
        print(name+","+realdate+","+location)
      comment=""
      for comment in main_frame.find_all("q", attrs={"class": "location-review-review-list-parts-ExpandableReview__reviewText--gOmRC"}):
        comment = comment.text
        print(comment+"\n")
      photos="No"
      for photo in main_frame.find_all("div", attrs={"class": "location-review-review-list-parts-SectionThumbnails__flex_grid--3KNhz"}):
          if(photo):
            photos="yes"
      print(photos)
      name = name.split(" ")
      gender_html = request.urlopen("https://api.genderize.io/?name="+name[0]).read()
      gendersoup = BeautifulSoup(gender_html,'html.parser')
      site_json=json.loads(gendersoup.text)
      gender= site_json['gender']
      print(gender)
      writer.writerow([date, "Mesón Sacristía de la Compañía", "TripAdvisor",name,gender,location,"",comment,photos,""])
  file.close




for i in range(0,2):
  url="https://www.tripadvisor.com.mx/Hotel_Review-g152773-d153885-Reviews-or"+str(5*i)+"-Meson_Sacristia_De_La_Compania-Puebla_Central_Mexico_and_Gulf_Coast.html"
# Make a GET request to fetch the raw HTML content
  html_content = requests.get(url).text
  soup = BeautifulSoup(html_content, "lxml")
  my_function(soup)


        
    
      
    