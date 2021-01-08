#!/usr/bin/env python
# coding: utf-8

# In[37]:


def loop(id):
    val=1
    n=1
    while(val!=id): 
        val=(val*7)%20201227
        if val==id: 
            return n 
        n+=1
    


# In[41]:


def find_key(idDoor,idCard): 
    valDoor=1
    valCard=1
    for i in range(1,loop(idDoor)+1): 
        valDoor= (valDoor*idCard)%20201227 
    for j in range(1,loop(idCard)+1):
        valCard=(valCard*idDoor)%20201227
    if valDoor == valCard:
        key=valDoor
        return i,j,key 
        


# In[42]:


print(find_key(17807724,5764801))


# In[ ]:




