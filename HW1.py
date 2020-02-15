#!/usr/bin/env python
# coding: utf-8

# Python Homework 1

# 1. Creating Python lists.  There is more than one way to do these!

# (a) [1,2,3,...,19,20]

# In[ ]:


a = range(1,21,1)
list(a)


# (b) [20,19,...,2,1]

# In[ ]:


b = range(20,0,-1)
list(b)


# (c) [1,2,3,...,19,20,19,18,...,2,1]

# In[ ]:


c = list(range(1,20,1))+list(range(20,1,-1))
c


# (d) [4,6,3,4,6,3,...,4,6,3],where there are 10 occurrences of 4. 

# In[ ]:


d = [4,6,3]*10
d.count(4)


# (e) [4,6,3, 4,6,3,...,4,6,3,4] where there are 11 occurrences of 4, 10 occurrences of 6 and 10 occur- 
# rences of 3. 

# In[ ]:


e = [4,6,3]*11
del e[-1]
from collections import Counter as co
co(e)


# 2. Create a list of the values of:  𝑒𝑥 cos(𝑥) for x=3, 3.1, 3.2, … 6.   

# In[ ]:


import numpy as np
x = np.arange(3,6.1,0.1)
re = [np.exp(i)*np.cos(i) for i in x]
re


#  Create a list of the values of: 

# In[ ]:


x = range(1,26,1)
re = [(2**i)/i for i in x]
re


# 4. Re-use your list from 1(a) as variable a.  It has length n. Create these lists: 

# (a) [a0 – an, a1 – an-1,…,an-a0] 

# In[ ]:


a = range(1,21,1)
re = [a[i-1]-a[20-i] for i in a]
re


# (b) A Boolean list where even values of a are True and odd values are False: [False, True,…].    
# 

# In[ ]:


a = range(1,21,1)
[a[i-1] % 2 == 0 for i in a]


# 5.Write a Python script that will open the file lorem.txt.  This is a bit of the “lorem ipsum”, nonsense Latin that’s used as a placeholder in publishing and graphic design.  Hint: Python strings have a method or two that might be helpful or you could use regular expressions.  The script will read the file and compute these quantities: 

# (a)  The number of strings whose lengths are:   between 1 and 4, between 4 and 7, and 8 or greater.

# In[9]:


with open("lorem.txt","r") as file:
    wz = file.read()
import re

q1 = re.findall(r"[\w]+",wz)


# In[10]:


def ju (x):
    return ((x != 1) & (x !=4) & (x !=7))

hh = [ju(len(i)) for i in q1].count(True)
"The number of strings, whose lengths between 1 and 4, between 4 and 7, and 8 or greater, is %s" % (hh)


# (b) The number of capitalized characters in the file.   

# In[ ]:


rss = re.findall(r"[A-Z]+",rs)


"the number of capitalized characters in the file is %s" % (len(rss))


# In[4]:


get_ipython().run_line_magic('pinfo', 'file.read')

