import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot


labels = ['AC', 'PC', 'LINUX']
colors = ['red', 'blue', 'yellow']
data = [2, 20, 1]


pyplot.pie(data, labels=labels, colors=colors, shadow=True)
pyplot.axis('equal')
pyplot.show()
