#!/usr/bin/env python
# coding: utf-8

# In[52]:


name = input("Name :")
print(f'Name : {name}')
tip = type(name)
print("type:", tip)

surname = input("Surname :")
print(f'Surname : {surname}')
print(type(surname))

age = input("Age :")
height = input("Height :")
print("Age :{} and Height :{}".format(age, height))

tip1 = type(int(age))
tip2 = type(float(height))
print("Type Age :{} and Type Height :{}".format(tip1, tip2))

weight = input("Weight :")
print(f'Weight : {weight}')
print(type(float(weight)))


# In[ ]:




