#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.


# In[2]:


a = int(input("Enter a value"))
b = int(input("Enter b value"))
c = int(input("Enter c value"))
s = int(input("Enter s value"))
class area_triangle:
    def __init__(self, a,b,c,s):
        self.s = s
        self.a = a
        self.c = c
        self.b = b
class Final_area(area_triangle):
    def area(self):
        print((s*(s-a)*(s-b)*(s-c)) ** 0.5)
Final = Final_area(a,b,c,s)
Final.area()
        
        
        
        


# In[ ]:





# In[3]:


def filter_long_words(lst, N):
    List =[]
    for i in lst:    
        if len(i)>N:
            List.append(i)
    print (List)
lst = []
n = int(input("Enter number of items to be in the list : "))
for i in range(0, n):
    ele = (input())
    lst.append(ele)
print(lst)
N = int(input("Enter the Number: "))

filter_long_words(lst, N)


# In[1]:


def map_func(lt):
    let=[]
    for i in lt:
        let.append(len(i))
    print(let)   
lt=[]
k = int(input("Enter number of items to be in the list : "))
for i in range(0, k):
    ele = (input())
    lt.append(ele)

map_func(lt)


# In[6]:


def character(i):
    L = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
    if i in L:
        print (True)
    else:
        print(False)
i = input("Enter a character: ")
character(i)


# In[ ]:




