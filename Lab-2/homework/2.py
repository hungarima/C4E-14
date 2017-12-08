from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
html_content = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn').read().decode('utf8')

soup = BeautifulSoup(html_content, 'html.parser')

data = []

#Table heading
tab_head = soup.find('table', {"id": "tblGridData"})
head_data_list = tab_head.find_all('td', 'h_t')
head_data = ['Trước Sau']
for td1 in head_data_list:
    head_data.append(td1.string.lstrip())

data.append(head_data)


#Table data
td_data_raw = []
tab_content = soup.find('table', {"id": "tableContent"})
content_list = tab_content.find_all('tr')
for tr in content_list:
    td_list = tr.find_all('td', style =  ['width:15%;padding:4px;color:#014377;', 'width:32%;color:#014377;', 'width:15%;padding:4px;color:#014377;font-weight:bold;', 'width:32%;color:#014377;font-weight:bold;'])
    tr_data = []
    for td in td_list:
        tr_data.append(td.text.strip())
    td_data_raw.append(tr_data)
td_data = [x for x in td_data_raw if x != []]
for i in range(len(td_data)):
    data.append(td_data[i])

print(data)



# data = [
#     [1, 21, 31],
#     [2, 22, 32],
#     [3, 23, 33],
#     [4, 24, 34],
#     [5, 25, 35],
#     [6, 26, 36]
# ]
pyexcel.save_as(array=data, dest_file_name="blah.xlsx")
