import bs4
import requests
from fake_useragent import UserAgent

ua = UserAgent()

HEADERS = {'User-Agent': str(ua.chrome)}
URL = 'https://habr.com/ru/'
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}


responce = requests.get(URL, headers=HEADERS)
text = responce.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    previews = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    previews = set(article.get_text().strip().split())
    if KEYWORDS & previews:
        href = article.find('h2').find('a').attrs.get('href')
        title = article.find("h2").find("a").find("span").text
        date = article.find('time').attrs.get('title')
        result = f'<{date}> - <{title}> - <{URL}{href}>'
        print(result)


