#!/usr/bin/env python
# coding: utf-8

# In[10]:


t=int(input("Enter no. of test case:"))
while t:
    n=int(input("Length of array:"))
    if n>10 or n<1:
        print("10>=n<=1")
        break                  
    arr=list(map(int,input().strip().split()))[:n]
    add=0
    for i in range(n):
        add+=arr[i]
    print("sum of element:"+format(add))
    t=t-1
    
        
    


# In[ ]:




