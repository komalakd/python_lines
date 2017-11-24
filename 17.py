import requests
from bs4 import BeautifulSoup

'''
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''

''' getting the html '''
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

''' parsing html '''
soup = BeautifulSoup(r_html, "html.parser")

''' getting the data '''
articles = soup.find_all('article')
#print articles.prettify()
print "New York Times today's articles: " + str(len(articles))

for article in articles:
	title = article.find('h2')
	if title:
		link = title.find('a')
		if link:
			print link.text.strip()
