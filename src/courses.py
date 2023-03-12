import requests
from bs4 import BeautifulSoup

cookie = {".ASPXAUTH": "YOUR_COOKIE", "ASP.NET_SessionId": "YOUR_COOKIE"}
response = requests.get(
    "https://online.udvash-unmesh.com/MasterCourse/Class?masterCourseId=2",
    cookies=cookie,
)
soup = BeautifulSoup(response.text, "html.parser")

links = [
    "https://online.udvash-unmesh.com" + link.get("href")
    for link in soup.find_all("a")
    if "&contentType=video" in link.get("href")
]
with open("lecture_links.txt", "w") as f:
    for link in links:
        f.write(link + "\n")

print(len(links))
