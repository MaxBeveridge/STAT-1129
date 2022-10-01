#!/usr/bin/env python
# coding: utf-8

# In[76]:


n=0
while n < 10:
    print(n)
    n+=1
    if n == 5:
        break


# In[77]:


n=0
while n < 5:
    print(n)
    n+=1
else: 
    print(n, 'is not less than 5')


# In[78]:


favorite_fruits = ['banana', 'orange', 'apple', 'lemon']
for f in favorite_fruits:
    if f != 'apple':
        print('I like', f)
    else:
        print(f, 'is really a fruit?')
        break


# In[79]:


n=0
t = 0
while n<=30:
    t=t+n
    n=n+1
print(t)


# In[80]:


grade = 100
if grade>=90:
    print('A')
elif grade>=80:
    print('B')
elif grade>=70:
    print('C')
elif grade>=60:
    print('D')
else:
    print('F')


# In[81]:


grades = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}
for n, g in grades.items():
    print(n, 'has a grade of', g)


# In[82]:


grades2=grades.values()
print(sum(grades2)/len(grades2))
print(max(grades2))
print(min(grades2))


# In[83]:


k = grades.keys()
for t in k:
    if 'J' in t:
        break
    print(t)


# In[84]:


k = grades.keys()
for t in k:
    if 'J' in t:
        continue
    print(t)

