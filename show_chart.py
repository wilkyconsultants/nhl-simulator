#!/usr/bin/env /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

print("Content-type: text/html\n\r\n")
#
# works, does not show in broswer, pops up window instead
#
# library and dataset
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
 
# Create data
df=pd.DataFrame({'x': range(1,101), 'y': np.random.randn(100)*15+range(1,101), 'z': (np.random.randn(100)*15+range(1,101))*2 })
 
# plot with matplotlib
plt.plot( 'x', 'y', data=df, marker='o', color='mediumvioletred')
plt.show()
 
# Just load seaborn and the chart looks better:
import seaborn as sns
plt.plot( 'x', 'y', data=df, marker='o', color='mediumvioletred')
plt.show()
