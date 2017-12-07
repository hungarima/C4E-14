from pymongo import MongoClient
#1. Connect to database
client = MongoClient("mongodb://admin:admin@ds129066.mlab.com:29066/c4e14-tth")

#2. Get default database
db = client.get_default_database()

#3. Get collection
blog = db['blog']

#4 Insert document
# new_post = {
#     'title': "Today is a rainy day",
#     'content': "I stay home coding"
# }
#
# blog.insert_one(new_post)

posts = blog.find() # GET ALL posts in blog
# print(posts[1])
for post in posts:
    print(post)
