#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
stem = pd.read_csv("C:/Users/Abhinav/Desktop/DataAnalysisCourseMaterials/DataAnalysis/data/STEM_Salaries.csv")
stem


# In[9]:


stem.shape


# In[29]:


STEM = stem.drop(labels=["Doctorate_Degree","Highschool","Some_College","Race_Asian","Race_White","Race_Black","Race_Two_Or_More","Race_Hispanic","Race","Education","otherdetails","dmaid","rowNumber","timestamp","Masters_Degree","Bachelors_Degree"],axis='columns')
STEM


# In[32]:


STEM.shape


# In[37]:


maang_companies =['Facebook','Apple','Amazon','Netflix','Google']
STEM_Maang = STEM[STEM['company'].isin(maang_companies)]
STEM_Maang


# In[56]:


summary = STEM_Maang.describe()
summary


# In[44]:


SFO_data = STEM_Maang [STEM_Maang['location'] == 'San Francisco, CA']
SFO_data


# In[45]:


Product_Manager = SFO_data [SFO_data['title'] == 'Product Manager']
Product_Manager 


# In[62]:


gender_counts = Product_Manager['gender'].value_counts()
gender_counts.plot(kind='bar')


# In[63]:


Product_Manager.boxplot(column='totalyearlycompensation', by='gender')


# In[64]:


Product_Manager.plot.scatter(x='yearsofexperience', y='totalyearlycompensation')


# In[65]:


company_distribution = Product_Manager['company'].value_counts()
company_distribution.plot(kind='pie', autopct='%1.1f%%')


# In[46]:


Experience_Years = Product_Manager[Product_Manager['yearsofexperience'] == 0]
Experience_Years


# In[66]:


Experience_Years = Product_Manager[(Product_Manager['yearsofexperience'] >= 0) & (Product_Manager['yearsofexperience'] <= 15)]
plt.figure(figsize=(10, 6))
plt.hist(Experience_Years['yearsofexperience'], bins=16, color='skyblue', edgecolor='black')
plt.xlabel('Years of Experience')
plt.ylabel('Number of Product Managers')
plt.title('Distribution of Product Managers by Years of Experience (0-15 years)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()


# In[ ]:




