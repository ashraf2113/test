
import requests
from bs4 import BeautifulSoup
import pandas as pd

job_title = []
company_name = []
location_name = []
skills = []
links=[]
salary=[]


result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
src = result.content
soup = BeautifulSoup(src, "html.parser")

jop_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_names = soup.find_all("a", {"class": "css-17s97q8"})
locations_names = soup.find_all("span", {"class": "css-5wys0k"})
jop_skills = soup.find_all("div", {"class": "css-1lh32fc"})

for i in range(len(jop_titles)):
    job_title.append(jop_titles[i].text)
    links.append(jop_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(locations_names[i].text)
    skills.append(jop_skills[i].text)  
    
for link in links:
    result=requests.get(link)
    src=result.content
    soup=BeautifulSoup(src,"html.parser")
    salaries=soup.find("span",{"class":"d9FyLd"},{" class":"hgKElc"},{"class":"MjjYud"})
    salary.append(salaries.text.strip())


data = {
    "Job Title": job_title,
    "Company Name": company_name,
    "Location": location_name,
    "Skills": skills, 
    "links":links,
    "salary":salary
}

df = pd.DataFrame(data)

df.to_csv("C:/Users/MEGA TECH/Desktop/python projects.csv", index=False)
