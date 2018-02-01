# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:33:18 2018

@author: dmink
"""

##Grabbing Corruption Perceptions Index Data 
import pandas as pd
corruptLink='https://raw.githubusercontent.com/EvansDataScience/data/master/corruption.csv'
CPI=pd.read_csv(corruptLink,encoding='Latin-1')

CPI.dtypes


#univariate exploration
#centrality
CPI['corruptionIndex'].describe() #descriptive statistics

#Dispersion
CPI['corruptionIndex'].std()/CPI['corruptionIndex'].mean() #finding coefficient of variation

#Skewness
CPI['corruptionIndex'].skew()

#Kurtosis
CPI['corruptionIndex'].kurtosis()

#visualizing distribution of CPI scores through a histogram
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

sns.distplot(CPI['CPI 2015 ScorecorruptionIndex'])
plt.legend(('data fit to normal','data as it is'))
plt.title('How are perceptions of corruption distributed between countries?')
plt.show()

#histogram with central measures
#statistics:
mnVar=CPI['corruptionIndex'].mean()
mdVar=CPI['corruptionIndex'].median()

sns.distplot(CPI['corruptionIndex'])
plt.title('Using central measures to determine position of outliers')
plt.axvline(mnVar, color='b', linestyle='dashed', linewidth=2,label='mean')
plt.axvline(mdVar, color='r', linestyle='dashed', linewidth=2,label='median')
plt.legend()

#making sure our CPI scores aren't affected by outliers
plot,dataBP=CPI['corruptionIndex'].plot.box(vert=False,return_type='both')

[value.get_xdata() for value in dataBP["boxes"]] # limits of the boxes

# box plot lines for min and max values, NOT considered outliers
[value.get_xdata() for value in dataBP["caps"]] 

CPI['corruptionIndex'].max()

# The 'caps' are computed usng the interquartile range (IQR).
# The IQR is the distance between the first and third quartile;
# or, in other terms, the distance between the 75th and 25th percentiles:

# 1. Computing 75th and 25th percentiles:
q25,q75=CPI['corruptionIndex'].quantile([0.25,0.75])

# 2. Computing the distance between them or IQR:
IQR=q75-q25

# which is:
IQR

capHigh = q75 + IQR*1.5
capHigh

capLow=q25 - IQR*1.5
capLow

#looks like we do not have any obvious outliers

##***PART B***

#bivariate analysis
pressLink='https://raw.githubusercontent.com/EvansDataScience/data/master/pressfreedom.csv'
press=pd.read_csv(pressLink,encoding='Latin-1')

indexes=pd.merge(CPI,press)

indexes.dtypes

# creating reversin function:
def reverse(aColumn):
    return max(aColumn) - aColumn + min(aColumn)

# reversing using function:
indexes['scorepressOK']=reverse(indexes.scorepress)

indexes.shape

indexes.iloc[:,[1,3]]

CPIscorepress=indexes.iloc[:,[1,3]]

CPIscorepress.corr()

pd.plotting.scatter_matrix(CPIscorepress,figsize=(12, 12))
plt.show()

import seaborn as sns
sns.pairplot(CPIscorepress.dropna())

CPIscorepress.corr(method='spearman')
