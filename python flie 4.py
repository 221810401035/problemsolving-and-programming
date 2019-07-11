#!/usr/bin/env python
# coding: utf-8

# 
# # Data structures
# 
# ## Dictionaries
# 
# # Dictionaries
# 
# 
# it works on the concept of set unique data
# keys.values is the unique identifier for a value
# 
# each key is separated from its values with colon(:)
# 
# each key and values is seperated by comma(,)
# 
# dictionaries enclosed with curly brackets({})
# 

# In[15]:


d1={"Name":"Gitam","Emailid":"Gitam@gmail.com","Address":"Hydrabad"}
print(d1)


# In[16]:


d1["Name"]


# In[17]:


d1['Emailid']='Gitam.python@gmail.com'
d1['Emailid']


# In[19]:


del d1['Emailid'] # deletes the specific key value


# In[20]:


d


# In[23]:


d1.keys() #returns the list of keys


# In[24]:


d1.values()# returns the values


# In[25]:


d1.items() # returns the list of tuples of keys and values


# # contact Application
# 
# 
# ## . Add contact
# ## . search the contact
# ## . list all contacts
# 
# ###    . Name1 : phone1
# 
# ###      . Name2 : phone2
# 
# ##  . Modify the contact
# 
# ##  . remove the contact
# 
# ##  . import the contact

# In[1]:


#Add contact
contacts = {} #creating a dict object
def addcontact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("contact details are added")
    else:
        print("contact details are already exists")
    return
addcontact('Phani','Gitam')
addcontact('Pavan','Gitam')
addcontact('Phani','Gitam')


# In[2]:


#search for contact details
def searchcontact(name):
    if name in contacts:
        print(name,":",contacts[name])
    else:
        print("%s does not exits" % name)
    return
searchcontact('Phani')
searchcontact('bunny')
searchcontact('Mani')


# In[3]:


# import some contacts 
# merge the contacts with excisting one
def importcontact(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"contacts added successfully")
    return
newcontacts={'pavan':9989324848,'Dhoni':9849101420}
importcontact(newcontacts)


# In[4]:


contacts


# In[7]:


#delete a contact
def deletecontact(name):
    if name in contacts:
        del contacts[name]
        print(name,"delete successfully")
    else:
        print(name,"not exists")
    return
deletecontact("Dhoni")    


# In[8]:


contacts


# In[14]:


#update the contact details
def deletecontact(name,phone):
    if name in contacts:
        contacts[name]=phone
        print(name,"update successfully")
    else:
        print(name,"not exists")
    return
deletecontact('Phani',9989324848)
deletecontact('prasad',9989765432)
    


# In[15]:


contacts


# # boolean True nor False
# 
# ## . islower: true if the string is lower case/false for all other cases
# 
# ## . isupper: true if the string is uppercase/false for all other cases
# 
# ## . istitle   :  true if the string is in titlecase/false
# 
# ## .isalpha : true if the string contacts only alphabets/false
# 
# ## .isnumeric : true if the contains only numbers/false
# 
# ## .isspace : true if the string has only space/false

# In[9]:


s1= 'GITAM'
print(s1.islower())
print(s1.isupper()) 


# In[10]:


S2="python programming"
s3="python programming"
print(s2.istitle())
print(s3.istitle())


# In[11]:


s2="Aplication1889"
s3="Pythonprogramming"
print(s2.isalpha())
print(s3.isalpha())


# In[12]:


s1="1234"
s2= "Aplication1779"
print(s1.isnumeric())
print(s2.isnumeric())


# In[14]:


s1=""
s2="Py th on"
print(s1.isspace())
print(s2.isspace())


# # string Methods
# 
# 
# ##   . join ()-- method will concatenate the two strings
# 
# ##  .split()--split() returns the list of strings separated by a whitespace(no parameter are       given)
# 
# 
# ## .replace()--replaces the specific word/character with new word/character

# In[2]:


s1 ='python'
print("".join(s1))


# In[3]:


s2 ="python programming easy to learn"
print(",".join(s2))


# In[4]:


li =['python','programming','learn']
print(",".join(li))


# In[6]:


s2 ="python programming easy to learn"
print(s2.split('a'))


# In[7]:


s2 ="python programming easy to learn"
li=s2.split()  #split the string--list object
print(li)
print(len(li))


# In[8]:


s2 ="python programming easy to learn"
print(s2.replace("gra","Application"))


# In[9]:


s2 = "python programming easy to learn"
li=list(s2)
print(li)


# In[10]:


s2 = "python programming easy to learn"
print(s2.replace("gra","Application"))


# # package and modules
# 
# 
# ## packages
#       
#       
# ###      - a collection of modules(single python files .py) and subpackages
# 
# 
# # '''module**
# 
# 
# ##       - a single python c=file containing set functions
# 
# # packages-->sub packages-->modules-->functions-->statements

# In[11]:


# import the externals packages to python file
import math
math.floor(123.45)


# In[12]:


from math import factorial as fact
fact(5)


# In[13]:


items=[1,5]
print("s",items)


# In[ ]:




