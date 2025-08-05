import pandas

import matplotlib.pyplot as plt

filename = 'indians-diabetes.data.csv'

hnames=['preg', 'plas', 'pres',
        'skin','test','mass',
        'pedi', 'age','class']

dataframe = pandas.read_csv(filename, names= hnames)
print(dataframe)

dataframe.hist()
plt.tight_layout()
plt.show()
