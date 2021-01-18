#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the different libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# In[93]:


#read the data from the .csv file
data = pd.read_csv('https://raw.githubusercontent.com/RichardThijs/Corona/main/owid-covid-data.csv', delimiter=',')
data


# In[100]:


x=data["cardiovasc_death_rate"]
y=data["female_smokers"]
x=np.array(x)
y=np.array(y)
print(x)
print(y)
y_min=y.min()
y_max=y.max()
print(y_min,y_max)


# In[101]:


# grafiek

fig=plt.figure()                                       # grafiekscherm

plt.xlim(0, 20)                                  # bereik op x-as
plt.ylim(0, 200)                                  # bereik op y-as
#myaxes.plot(y,x)
plt.title("dodental, leeftijdsgroep")    # titel geven aan grafiek
plt.xlabel("cardiovasc_death_rate")                              # omschrijving geven bij x-as
plt.ylabel("female_smokers")                    # omschrijving geven bij y-as

plt.scatter(x,y)        # puntenwolk, kleur en vorm van punten vastleggen

plt.show()     
# grafiek tonen

