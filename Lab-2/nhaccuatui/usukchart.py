from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
html_content = urlopen('https://www.nhaccuatui.com/top100/top-100-pop.zE23R7bc8e9X.html').read().decode('utf8')

soup = BeautifulSoup(html_content, 'html.parser')
ul = soup.find('ul', 'list_show_chart')
li_list = ul.find_all('li')

music_list =[]

for li in li_list:
    div = li.find('div', 'box_info_field')
    h4 = div.find('h4')
    singers_list = h4.find_all('a')

    singers = ''
    for a in singers_list:
        singers += a.string + ' '

    music = {
        'title': div.h3.a.string,
        'singer': singers
    }
    music_list.append(music)

pyexcel.save_as(records= music_list, dest_file_name ="nct.xlsx")
