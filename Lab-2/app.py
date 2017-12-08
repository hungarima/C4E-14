from urllib.request import urlopen
from bs4 import BeautifulSoup # Camel Case
import pyexcel
#1. Download page
webpage = urlopen('http://dantri.com.vn') #Open connection
data = webpage.read()
html_content = data.decode('utf8')

#2. Analyze ROI (Region Of Interest)
#2.1 Creat Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())
ul = soup.find('ul', 'ul1 ulnew') # find one
li_list = ul.find_all('li')

# print(li_list[0].prettify())
# for li in li_list:
#     print(li.prettify())
#     print("*" * 100)

news_list = []

for li in li_list:
    a = li.h4.a # find('a')
    news = {
        'title': a.string,
        'link' : a['href']
    }
    news_list.append(news)

# print(news_list)
pyexcel.save_as(records= news_list, dest_file_name="dantri.xlsx")



#3. Extract data from ROI
