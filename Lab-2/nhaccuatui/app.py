from urllib.request import urlopen
html_content = urlopen('https://www.nhaccuatui.com/').read()

file = open('nct.html', 'wb') # w = write, b = binary (raw)
file.write(html_content)
file.close()
