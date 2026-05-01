from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
site_html = response.text

soup = BeautifulSoup(site_html,"html.parser")
# print(soup.prettify())
with open("yc_website_html.html", "w") as file:
    file.write(soup.prettify())


# all_anchor_tags = soup.find_all("a")
# for a_tag in all_anchor_tags:
#     print(a_tag.get("href"))

# count = 0
# article_info = {}
#
# all_a_tags = soup.select(selector=".title .titleline a")
#
# for a_tag in all_a_tags:
#     count += 1
#     if count % 2 == 0:
#         pass
#     else:
#         article_info[a_tag.getText()] = [a_tag.get("href")]
# print(article_info)
#
# scores = soup.find_all(class_="score")
# all_score = []
# for score in scores:
#     all_score.append(score.getText())

# dict -> {1:{title:_title_},{link:_link_},{score=_score_},2:{..}}
# dict -> {_title_:[_link_,_score_]}


count = 0
article_link = []
article_title = []
article_score = []
# ".titleline > a" to get direct children of the parent element
all_a_tags = soup.select(selector=".title .titleline > a")
for a_tag in all_a_tags:
    article_link.append(a_tag.get("href"))
    article_title.append(a_tag.getText())
scores = soup.find_all(class_="score")
for score in scores:
    article_score.append(score.getText())
# print(article_title)
# for _ in range(len(article_title)):
#     print(f"The article '{article_title[_]}' can be accessed on site {article_link[_]} and has an upvote of {article_score[_]}.")

score_int = [int(score.split()[0]) for score in article_score]

article_info = {}
# dict -> {_title_:[_link_,_score_]}
for name,link,score in zip(article_title,article_link,score_int):
    article_info[name] = [link,score]

highest_score_index = score_int.index(max(score_int))
print(f"The article with highest upvotes is titled : '{article_title[highest_score_index]}' can be accessed on site {article_link[highest_score_index]} and has an upvote of {article_score[highest_score_index]}.")




# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# all_a_tags = soup.find_all(name="a")
# for a_tag in all_a_tags:
#     print(a_tag.get("href"))
#
# heading = soup.find(name="h1",id = "name")
# print(heading)

