from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL
html_content = urlopen('https://www.apple.com/itunes/charts/songs/').read().decode('utf8')


soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find('section', 'section chart-grid')
div = section.find('div', 'section-content')
li_list = div.ul.find_all('li')

music_list = []

for li in li_list:
    musics = {
        'title': li.h3.a.string,
        'singer': li.h4.a.string
    }
    music_list.append(musics)

pyexcel.save_as(records = music_list, dest_file_name ="itunes.xlsx")

options = {
    'default_search': 'ytsearch',
    'max_downloads': len(music_list),
    'format': 'bestaudio/audio'
}

dl= YoutubeDL(options)
for music in music_list:
    dl.download([music['title']])
