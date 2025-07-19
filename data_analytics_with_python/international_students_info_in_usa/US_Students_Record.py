#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd

file_path = 'C:/Users/Abhinav/Desktop/Data Analytics/US_Students_Records.xlsx'

# Loading the XLSX file
record = pd.read_excel(file_path)

# Displaying the first few rows to verify the data was loaded
df.head()


# In[82]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a line plot to show the trend over the years.
plt.figure(figsize=(12, 6))
ax = sns.lineplot(data=record, x='Year', y='Total', marker='o', markersize=5, color='b', label='Total Students')
plt.title('Trend of Total International Students from All Continents Going to the USA')
plt.xlabel('Year')
plt.ylabel('Total Number of Students')

# Setting x-axis ticks at 5-year intervals
xticks = range(0, len(record['Year']), 5)
xlabels = record['Year'].iloc[xticks].apply(lambda x: x.replace('/', '-'))
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels, rotation=45)

plt.legend(loc='upper left')
plt.grid(True)
plt.show()


# In[93]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a line plot for the selected continents.
selected_continents = [
    'Asia', 'East_Asia', 'South_and_Central_Asia', 'Southeast_Asia'
]

# Defining the years for custom x-axis labels.
custom_years = ['1949-50', '1974-75', '1999-00', '2004-05', '2009-10', '2014-15', '2019-20']

# Creating a mapping from custom years to the closest available data points.
custom_years_to_data_index = {
    '1949-50': 0,
    '1974-75': 5,
    '1999-00': 10,
    '2004-05': 15,
    '2009-10': 20,
    '2014-15': 25,
    '2019-20': 30
}

plt.figure(figsize=(12, 6))
for column in selected_continents:
    sns.lineplot(data=record, x='Year', y=column, label=column)

plt.title('Number of Students from Selected Asian Regions Going to the USA')
plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.legend(loc='upper left')
plt.grid(True)

# Expanding the vertical axis.
plt.ylim(bottom=0)

# Setting custom x-axis ticks and add labels at the end of each line.
plt.xticks([custom_years_to_data_index[year] for year in custom_years], custom_years, rotation=45)

for column in selected_continents:
    x_pos = custom_years_to_data_index['2019-20']
    y_pos = record[column].iloc[x_pos]
    plt.text(x_pos, y_pos, column, va='center', ha='left', backgroundcolor='w')

plt.show()


# In[102]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setting a Seaborn style with a dark grey background
sns.set(style="darkgrid")

# Creating a color palette
colors = sns.color_palette("husl")

# Creating a line plot for the selected continents.
selected_continents = [
    'Asia', 'East_Asia', 'South_and_Central_Asia', 'Southeast_Asia'
]

# Defining the years for custom x-axis labels.
custom_years = ['1949-50', '1974-75', '1999-00', '2004-05', '2009-10', '2014-15', '2019-20']

# Creating a mapping from custom years to the closest available data points.
custom_years_to_data_index = {
    '1949-50': 0,
    '1974-75': 5,
    '1999-00': 10,
    '2004-05': 15,
    '2009-10': 20,
    '2014-15': 25,
    '2019-20': 30
}

# Creating a dark grey background
plt.figure(figsize=(12, 6))
ax = plt.gca()
ax.set_facecolor('#333333')  # Dark grey background

for i, column in enumerate(selected_continents):
    sns.lineplot(data=record, x='Year', y=column, label=column, color=colors[i], linestyle='-', linewidth=2, marker='o')

plt.title('Number of Students from Selected Asian Regions Going to the USA')
plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.legend(loc='upper left')
plt.grid(True, color='white', linestyle='--')

# Expanding the vertical axis.
plt.ylim(bottom=0)

# Setting custom x-axis ticks and add labels at the end of each line.
plt.xticks([custom_years_to_data_index[year] for year in custom_years], custom_years, rotation=45)

# Adding values to the x-axis labels
for year in custom_years:
    x_pos = custom_years_to_data_index[year]
    for column in selected_continents:
        y_pos = record[column].iloc[x_pos]
        plt.text(x_pos, y_pos, f'{y_pos}', va='bottom', ha='center', backgroundcolor='w', color='black', fontsize=9)

plt.show()


# In[ ]:




