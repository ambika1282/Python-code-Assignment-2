#!/usr/bin/env python
# coding: utf-8

# In[1]:



def myreduce( sum,l):
            return a
def sum(a,b) :
            return a+b

l=[1,5,9,7]
a=l[0]
for i in range(1,len(l)):
        b=l[i]
        a=sum(a,b)
print(myreduce( sum,l))
        
    
    


# In[2]:


def myfilter(is_even,list_1):
    return is_even(a)
list_1=[1,2,3,4,5,6,7,8,9]
list_2=[]
def is_even(a):
    for i in list_1: 
        if i%2 == 0:     
            list_2.append(i) 
    print(list_2)
myfilter(is_even,list_1)


# In[3]:


l='xyz'
[i*j for j in [1,2,3,4] for i in l ]


# In[4]:


l='xyz'
[j*i for i in l for j in [1,2,3,4]  ]


# In[5]:


l=[2,3,4]

[[i+j]  for j in [0,1,2] for i in l ]


# In[6]:


[[i+j] for i in range(2,5) for j in range(0,3)]


# In[7]:


l=[2,3,4,5]
[[i+j   for i in l] for j in range(0,3)  ]


# In[57]:


l=[1,2,3]
[(i,j)  for j in range(1,4) for i in l   ]


# In[ ]:




