import requests
from bs4 import BeautifulSoup

URL = "https://in.indeed.com/jobs?q=data+engineer&l=India&from=search&vjk=5079cef27dae2d1d"
page = requests.get(URL)

# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
print(soup)
job_postings = soup.find_all("div", {"class": "jobTupleHeader"})
print(job_postings)
