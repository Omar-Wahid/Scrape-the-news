from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
tag = soup.find_all(class_="titleline")
tag_anchor = [item.find("a") for item in tag]
article_text = [item.getText() for item in tag_anchor]
article_link = [item.get("href") for item in tag_anchor]

article_score = [int(votes.getText().split()[0]) for votes in soup.find_all(name="span", class_="score")]
max_index = article_score.index(max(article_score))
print(article_text[max_index])
print(article_link[max_index])
print(article_score[max_index])

print(max_index)
