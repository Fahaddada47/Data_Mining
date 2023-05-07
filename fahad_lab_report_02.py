# -*- coding: utf-8 -*-
"""Fahad_lab_report_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fB52rtI2HtXimG7x7i-B0UyzQtKvgPma

# **Lab Report 01**
**Name:Fahad Islam**

**ID:193002039**
"""

import pandas as pd

"""**Import Dataset**"""

from google.colab import files
 
 
uploaded = files.upload()
df=pd.read_csv('loan_data_set.csv')

"""**Read Dataset**"""

df.head()

"""**Number of Columns and rows of data**"""

df.shape

import seaborn as sns

"""***Convert the Loan_Status column into 0/1 ***



"""

yn_map = {'Y': 1, 'N': 0}

df['Loan_Status']=df['Loan_Status'].map(yn_map)

df.head()

""" **Number of people taking loan**"""

sns.countplot(x ='Loan_Status', data = df)
df['Loan_Status'].value_counts()

df['Loan_Status'].value_counts().plot(kind='bar')

"""**Number of married and unmarried people**"""

yn_map = {'Yes': 1, 'No': 0}

df['Married']=df['Married'].map(yn_map)

df.head()

sns.countplot(x ='Married', data = df)
df['Married'].value_counts()

"""**Pie chart for people who has dependents **"""

df['Dependents'].value_counts().plot(kind='pie' ,autopct='%.2f')

"""**Bar for people according to theri income**"""

import matplotlib.pyplot as plt
plt.hist(df['ApplicantIncome'],bins=15,rwidth=0.8)

"""**Displot of people and their income**"""

sns.distplot(df['ApplicantIncome'], bins=15, kde=True)

"""# **Boxplot of applicants Income**

"""

sns.boxplot(df['ApplicantIncome'])

"""**Here we can see the density amountof applicant income *"""

sns.violinplot(x='ApplicantIncome',data=df)

"""**Here is the bar graph of people who has dependents and their loan Amount *"""

sns.barplot(data=df,x='Dependents',y='LoanAmount')

"""# For evey gender who has dependents and their loan number """

sns.barplot(data=df,x='Dependents',y='LoanAmount',hue='Gender')

"""**Separate boxplot for all gender and their Income**"""

sns.boxplot(data=df,x='Gender',y='ApplicantIncome')

"""**Separate boxplot for all gender and their Income also their dependents**"""

sns.boxplot(data=df,x='Gender',y='ApplicantIncome',hue="Dependents")

"""# **Convert value for counting**"""

yn_map = {'Yes': 1, 'No': 0}

df['Self_Employed']=df['Self_Employed'].map(yn_map)

df.head(10)

"""**For missing value input 0 becasuse there are only two option so that can't be factional valoue using mean()**"""

df['Self_Employed'] = df['Self_Employed'].fillna(0)

df.head(10)

"""**For missing value input 0 becasuse there are only two option so that can't be factional valoue using mean()**"""

yn_map = {'Graduate': 1, 'Not Graduate': 0}

df['Education']=df['Education'].map(yn_map)

df.head()

"""**There are 117 non self employed who is not graduate **
**There are 17 self employed who is not graduate **
**There are 415  self employed who is not graduate **
**There are 117  not self employed who is  graduate **
"""

pd.crosstab(df['Education'],df['Self_Employed'])

"""**Heat map for visual that people's emplument according to their education**"""

sns.heatmap(pd.crosstab(df['Education'],df['Self_Employed']))

"""**480 people are graduate and 134 people are not graduate**"""

sns.countplot(x ='Education', data = df)
df['Education'].value_counts()

"""**Another way to count Educated peole and their employment **"""

count_df = df.groupby(['Education', 'Self_Employed']).size().reset_index(name='Count')

print(count_df)

"""**Number of employed poeple whos is taking loan**"""

count_df = df.groupby(['Self_Employed', 'Loan_Status']).size().reset_index(name='Count')

print(count_df)

"""**Pairplot for employed people and loan status**"""

sns.pairplot(count_df)

import seaborn as sns

"""df = sns.load_dataset('loan_data_set')"""

from google.colab import files
uploaded = files.upload()

df1=pd.read_csv('titanic.csv')

df1.head(1)

df1 = sns.load_dataset('titanic')

df1.head(5)

"""**Displot accodring married people and their loan status**"""

sns.distplot(df[df['Married']==0]['Loan_Status'],hist=False,color="red")
sns.distplot(df[df['Married']==1]['Loan_Status'],hist=False)

"""**Number of married people and taking loan**"""

df.groupby('Married').mean()['Loan_Status']*100

"""**Average loan status of peoples dependent**"""

df.groupby('Dependents').mean()['Loan_Status']*100

"""**Total number of 2 catagories of peole and their status according to theri education**"""

df.groupby('Education').sum().reset_index()

"""**Total number of 2 catagories of peole and their status according to theri loan status**"""

new = df.groupby('Loan_Status').sum().reset_index()

new.head()

"""**Here is the line plot for peoples marriage status and their loan status**"""

sns.lineplot(data=new, x="Married", y="Loan_Status")