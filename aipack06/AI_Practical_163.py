import pandas

import matplotlib.pyplot as plt

filename = 'indians-diabetes.data.csv'

hnames=['preg', 'plas', 'pres',
        'skin','test','mass',
        'pedi', 'age','class']

dataframe = pandas.read_csv(filename, names= hnames)
dataframe.plot(kind='box',subplots=True,
               layout=(3,3),sharex=False,
               sharey=False)


plt.show()
