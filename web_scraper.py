import requests
from bs4 import BeautifulSoup
import json

with open("11_JSTOR_ Search Results.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

titles = []
authors = []
## Code to get the all the article titles 
for article in soup.find_all("a", "link-no-underline"):
    titles.append(article.text)

for author in soup.find_all("div", "contrib metadata-row"):
    authors.append(author.text)


# Create the dictionary to be converted to JSON 
if len(titles)==len(authors):
    data = {}
    data['articles'] = []
    for index, title in enumerate(titles):

        info = {'title':title, 'authors':authors[index]}
        data['articles'].append(info)
else:
    print ("different lengths of titles and authors")

#  Convert to JSON
with open('data_10.txt', 'w') as outputfile:
    json.dump(data, outputfile)

