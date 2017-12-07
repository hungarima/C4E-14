from gmail import GMail, Message
from random import *

reasons = [
    'thương hàn',
    'ebola',
    'thuỷ đậu'
]

template1 ='''<h2><strong>ĐƠN XIN PH&Eacute;P NGHỈ HỌC</strong></h2>
<p><em><strong>Ch&agrave;o chị Huy,</strong></em></p>
<p>Khoẻ kh&ocirc;ng anh&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></p>
<p>H&ocirc;m nay em dính {{randreason}} n&ecirc;n kh&ocirc;ng đi học được nh&eacute;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></p>
<p>&nbsp;</p>'''

template2 ='''<h2><strong>ĐƠN XIN ĐƯỢC NGHỈ HỌC</strong></h2>
<p><strong><em>Hello chị Huy,</em></strong></p>
<p><strong><em>H&ocirc;m nay đầu em n&oacute; c&oacute; nhức nhức kiểu g&igrave; &yacute; cho em nghỉ nh&eacute;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-laughing.gif" alt="laughing" /></em></strong></p>
<p><strong><em><img src="http://i0.kym-cdn.com/photos/images/newsfeed/000/096/044/trollface.jpg?1296494117" alt="" width="640" height="640" /></em></strong></p>'''


templates = [template1, template2]


randtem = choice(templates)
randreason = choice(reasons)
html_content = randtem.replace("{{randreason}}", randreason)
gmail = GMail('c4e14.labs.tth@gmail.com', 'c4e14labs')
msg = Message('HELLO', to='tronghung199@gmail.com', text='Today is a good day to die', html=html_content)

import datetime

now = datetime.datetime.now()
print(now.hour)
while True:
    if now.hour == 7:
        gmail.send(msg)
        False
        break
