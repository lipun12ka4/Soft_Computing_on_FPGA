import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.__version__

utilization=pd.read_excel("UtilizationTable.xlsx")
# utilization.head()

# print(utilization.to_string())

UtilPercent = utilization[['Resource','Utilization %']]
# print(UtilPercent.to_string())

x_labels = UtilPercent.Resource
# print(x_labels)

# plt.figure(figsize=(12, 8))
# ax = UtilPercent.plot(kind='bar')
# ax.set_title("Utilization Report")
# ax.set_xlabel("Resources")
# ax.set_ylabel("Percent of Utilization")
# ax.set_xticklabels(x_labels)

UtilPercent['Free %'] = UtilPercent['Utilization %'].apply(lambda x: 100 - x)
# print(UtilPercent.to_string())

# my_colors = 'bmkrmg'  #red, green, blue, black, etc.
my_colors = ['blue','greenyellow']

# plt.figure(figsize=(12, 8))
ax = UtilPercent.plot(kind='barh', stacked=True, color=my_colors)
ax.set_title("Utilization Report", fontsize=18)
ax.set_ylabel("Resources", fontsize=17)
ax.set_xlabel("Percent of Utilization", fontsize=17)
ax.set_yticklabels(x_labels, fontsize = 'large')

for i, v in enumerate(UtilPercent['Utilization %'].astype('float64').round(2)):
    ax.text(v +3, i - .08, str(v) + ' %', color='black', fontsize=14, fontweight='bold')

plt.show()