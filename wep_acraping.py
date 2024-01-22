
import requests 
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import pandas as pd
jop_title=[]
company_name=[]
location_name=[]
skills=[]
links=[]
salary=[]


result=requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
src=result.content
#print(src)
soup=BeautifulSoup(src,"lxml")
#print(soup)
jop_titles=soup.find_all("h2",{"class":"css-m604qf"})
company_names=soup.find_all("a",{"class":"css-17s97q8"})
locations_names=soup.find_all("span",{"class":"css-5wys0k"})
jop_skills=soup.find_all("div",{"class":"css-1lh32fc"})

for i in range(len(jop_titles)):
    jop_title.append(jop_titles[i].text)
    links.append(jop_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(locations_names[i].text)
    skills.append(jop_skills[i].text)
for link in links:
    result=requests.get(link)
    src=result.content
    soup=BeautifulSoup(src,"lxml")
    salaries=soup.find("span",{"class":"d9FyLd"},{" class":"hgKElc"},{"class":"MjjYud"})
    salary.append(salaries.text.strip())
