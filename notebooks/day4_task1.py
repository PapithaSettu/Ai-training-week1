#!/usr/bin/env python
# coding: utf-8

# 

# In[ ]:


a=10
b=20
print(a+b)



# In[2]:


a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("Addition:,a+b")


# In[ ]:




# # Week 1-Day 4
# ## Python $ Data Engineering
# ### Task 1 - jupyter Notebook

# In[4]:


numbers=list(range(1000))
%timeit [x * 2 for x in numbers]


# In[5]:


def multiply_numbers():
    result=[]
    for x in numbers:
        result.append(x * 2)
    return result

%timeit multiply_numbers()        

# In[1]:


print("hello world")

# In[6]:


numbers=list(range(1000))


# In[7]:


%timeit [x * 2 for x in numbers]


# In[8]:


%%timeit
result=[]
for x in numbers:
    result.append(x * 2)

# ## notebook vs python file
# 1.jupyter Notebook is useful for learning,testing code,and data analysis.
# 2.it allows us to execute code cell by cell.
# 3.python(.py) files are useful for devloping applications and automation.
# 4.python files are suitable for reusable code and production projects.

# ## performance comparision
# 
# List comprehension and for loop are two ways to process lists.
# List comprehension is generally faster and mofe concise.
# %timeit measures the execution time of python code

# 
