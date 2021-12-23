 #//requests.org
import requests 
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

# print(indeed_soup);
pagination = indeed_soup.find("div", {"class": "pagination"})

print(pagination)

# page= pagination.find_all("a")

# print(page)