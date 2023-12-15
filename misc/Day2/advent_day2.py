#!/usr/bin/env python
# coding: utf-8

# In[15]:


#read line to get number of password entered 
file= open("day2data.txt","r")
line=file.readlines() #each line store as one element of a string array


# In[20]:


#append all charctaer in one line in an array 
bigCount=0
num_line=0
while num_line<len(line): 
    #append all character in a line to an array
    arr=[]
    for char in line[num_line]:
        arr.append(char)
    #set up min max letter 
    min=int(arr[0])
    max=int(arr[2])
    letter=arr[4]
    #find the start of the password
    i=0
    while i<len(arr):
        if arr[i]==":" and arr[i+1]==" ":
            start=i+2
            break
        i+=1
    #append the passcode to arr2         
    arr2=[]
    j=start
    while j<(len(arr)-1):
        arr2.append(arr[j])
        j+=1
    count=0 #this will count how many time the letter appear 
    for k in range(len(arr2)):
        if arr2[k]==letter:
            count+=1
    if count>=min and count<=max: 
            bigCount+=1
    
    num_line+=1

    


# In[21]:


print(bigCount)


# In[ ]:




