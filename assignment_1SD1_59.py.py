#!/usr/bin/env python
# coding: utf-8

# In[31]:


#1
n = []
lower = 2000
upper = 3200

for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        n.append(str(x))
print(','.join(n))


# In[ ]:





# In[40]:


#2
str_1= 'Srushti Shriad Kulkarni'

s = str_1[: : -1]

p = str_1.upper()

print(s)
print(p)


# In[ ]:





# In[41]:


#3

d = 12
pi = 3.14

volume = 4/3 * pi * (d/2)**3

print(volume)


# In[ ]:




