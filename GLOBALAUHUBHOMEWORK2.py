#!/usr/bin/env python
# coding: utf-8

# In[3]:


firstname = input("First Name : ")
lastname = input("Last Name : ")
age = int(input("Age : "))
dateofbirth = int(input("Date of Birth -just year- : "))
mylist = [firstname, lastname, age, dateofbirth]
print(mylist)
for i in range(1):
    if age < 18:
        print("You can't go out because it's too dangerous.")
    else:
        print("You can go out to the street.")


# In[ ]:




