#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[92]:


# Load the data into a DataFrame
data = pd.read_csv("C:/Users/dell/Desktop/OPS Free internship/traces_data.csv")
'''Here I modified the column names
As the column names was creating problem for extracting the columns for data analysis
a: Timestamp
b: traceID
c: spanID
d: parentSpanID
e: serviceName
f: Name
g: durationNano'''


# In[93]:


# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(data.head())


# In[94]:


# Summary statistics of numerical columns here only durationNano
print("\nSummary statistics of numerical columns:")
print(data.describe())
#Here g stands for durationNano which is only one numerical column


# In[95]:


# Check for missing values
print("\nMissing values in the dataset:")
print(data.isnull().sum())


# In[96]:


# Distribution of durationNano
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='g', bins=30,alpha= 0.7, kde=True)
plt.title("Distribution of durationNano")
plt.xlabel("Duration (nanoseconds)")
plt.ylabel("Frequency")
plt.show()
#The distribution of durationNano is strictly positively skewed 


# In[83]:


# Count of spans per serviceName
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='e')
plt.title("Count of spans per serviceName")
plt.xlabel("Service Name")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
#This shows that total number of payment service is maximum among all services and frontend-web is least among all services


# In[97]:


# Boxplot of Duration by Service Name
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='e', y='g')
plt.title("Boxplot of Duration by Service Name")
plt.xlabel("Service Name")
plt.ylabel("Duration (nanoseconds)")
plt.xticks(rotation=45)
plt.show()
#This shows that frontend-proxy has a outlier present and also frontend service has fur outliers present 


# In[98]:


# Barplot of Average Duration by Service Name
plt.figure(figsize=(12, 6))
sns.barplot(data=data, x='e', y='g', estimator=np.mean)
plt.title("Average Duration by Service Name")
plt.xlabel("Service Name")
plt.ylabel("Average Duration (nanoseconds)")
plt.xticks(rotation=45)
plt.show()
'''This is an interesting plot as we have seen earlier that
frontend web services has lowest number of service but the duration nano is quite high
and payment srvices had maximum number of counts as service provider but durationNAno is quite low for them
frontend services has maximum average duration time 
So it can be stated that maximum service providers has lesser duration'''


# In[99]:


# Countplot of Method Name by Service Name
plt.figure(figsize=(12, 6))
sns.countplot(data=data, x='e', hue='f')
plt.title("Count of Method Name by Service Name")
plt.xlabel("Service Name")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend(title='Method Name', bbox_to_anchor=(1, 1))
plt.show()
'''It shows that payment services has used maximum number of method named fs statSync'''


# In[ ]:




