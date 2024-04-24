#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
def generate_name():
    first_names=["Sasha","Chandler","Rebecca","Tom","Claudie","Hensley","Kurtis","Hillary","Heather","Lena","Polly","Fred","Belcalis","Monne","George","Dennis"]
    last_names=["McFlaire","Jonas","Klum","Felix","Carter","Sawyer","Coleman","Starr","Elnis","Frauman","Dickens","Almond","Hermann","Molk","Versay","Leighton"]
    return "{} {}".format(random.choice(first_names), random.choice(last_names))
for i in range(1):
    print(generate_name())


# In[ ]:




