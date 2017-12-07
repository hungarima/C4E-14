from pymongo import MongoClient
client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")

db = client.get_default_database()

blog = db['posts']

new_post = {
    "title": "Lạ Lùng",
    "author": "TH",
    "content": "Có những khoảnh khắc như thế này trong đời, định đứng dậy để làm một điều gì đó có nghĩa, nhưng lại e dè từ chối bản thân. Tôi là như vậy, sự thiếu quyết đoán của bản thân làm mọi cơ hội trong cuộc sống, trong tình yêu tiêu tan hết. Trải qua cảm giác gần cô ấy lắm nhưng không chạm được, gần cô ấy lắm nhưng không sao mở lời được, chỉ thấy lạ lùng cô đến rồi cô đi, như nắng đến thì giấc mơ bay đi, đành thôi. Tôi lại ngồi nhớ em!"
}

blog.insert_one(new_post)
