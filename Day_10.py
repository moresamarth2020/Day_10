#!/usr/bin/env python
# coding: utf-8

# # Excersice 2: Good Morning Sir:
# - Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:

# In[1]:


import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)


# In[16]:


# Take input from the user
hour = input("Enter the hour of the day (0-23): ")

# Check if the input is a valid integer
if hour.isdigit():
    hour = int(hour)
    if 0 <= hour < 24:
        if 5 <= hour < 12:
            print("Good Morning!")
        elif 12 <= hour < 17:
            print("Good Afternoon!")
        elif 17 <= hour < 21:
            print("Good Evening!")
        else:
            print("Hello! It's a bit late, take care.")
    else:
        print("Invalid hour! Please enter a value between 0 and 23.")
else:
    print("Please enter a valid number.")


# In[ ]:





# In[ ]:




