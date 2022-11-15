#!/usr/bin/env python
# coding: utf-8

# In[7]:


n= int(input())
m = int(input())

i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break
print()

