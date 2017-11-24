import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

print soup.find(class_='hed').text
print soup.find(class_='dek').text

for x in xrange(1,10):
	 pass


	 