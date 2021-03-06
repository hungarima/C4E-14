from pymongo import MongoClient
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")

db = client.get_default_database()

customers = db['customers']
lis_custs = customers.find()
count = 0

labels = ['Events', 'Advertisements', 'Word of mouth']
colors = ['#FEBFB3', '#E1396C', '#96D38C']
events = ads = wom = 0
for customer in lis_custs:
    if customer["ref"] == "ads":
        ads += 1
    elif customer["ref"] == "wom":
        wom += 1
    elif customer["ref"] == "events":
        events += 1
data = [events, ads, wom]
print("Events:", events)
print("Ads:", ads)
print("Wom:", wom)
pyplot.pie(data, labels = labels, colors = colors, autopct='%1.1f%%', shadow = True)
pyplot.axis('equal')
pyplot.show()
