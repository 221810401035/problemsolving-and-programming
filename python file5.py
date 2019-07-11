#!/usr/bin/env python
# coding: utf-8

# # standard libraries
# 
# 
# 
# ##     . file l/o
# ##     . regular expressions
# ##     . datetime
# ##     . math (numerical and mathematics)
# 
# 
# 
# 
# 
# #     write,read,Analysis--data science and analysis
# 
# 
# 
# 
# 
# ##    file handling in python
# 
# 
# 
# ###   . file:-document containing information resides on the permanent storage
# 
# ###   . different types of files :-txt.doc.pdf.csvetc....
# 
# ###   . input--keyboard
# 
# ###   . output--file
# 
# 
# #   modes of the file l/o
# 
# ###   . 'w'-- this mode is used to file writing
# 
# 
# ###           ---- if  the is not present first it created the file and write some  data to it
# 
# ###           ---if the files is already present  it will rewrite the previous contact     

# In[1]:


# function to created a file and write to the file 
def createfile(filename):
    f= open(filename,'w')
    for i in range(10):
        f.write('this is %d line\n' % i)
    print("file is created and data has written")
    return
createfile('file.txt')


# In[2]:


ls


# In[3]:


def createfile(filename):
    f=open(filename,'w')
    f.write('testing.....\n')
    print("file is created and data has written")
    return
createfile('file.txt')


# In[5]:


def appenddata(filename):
    f=open(filename,'a')
    for i in range(10):
        f.write('this is %d line \n' % i)
    print("file is created and data has written successfully")
    return
appenddata('file2.txt')           


# In[6]:


def appenddata(filename):
    f=open(filename,'a')
    f.write('new line 1 \n')
    f.write('new line 2 \n')
    f.write('')
    print("file is created and data has written successfully")
    return
appenddata('flie2.txt')


# In[7]:


# function to read the file
def readfiledata(filename):
    f = open(filename,'r')
    if f.mode =='r':
        x = f.read()
        print(x)
    f.close()
    return
readfiledata('file2.txt')


# In[1]:


#finction to read the files
def fileoperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode == 'r':
            data = f.read()
            print(data)
        elif f.mode =='a':
            f.write('Data to the file')
            print('The data successfully written')
    f.close()
    return
filename=input('Enter the file name')
mode=input('Enter the mode of the file')
fileoperations(filename,mode)
            


# In[2]:


#data analysis
#word count program
def wordcount(filename,word):
    with open(filename,'r') as f:
        if mode == "r":
            x=f.read()
            li=x.split() #its splits the string with whitespace
    cnt-li.count(word)
    return cnt
filename = input('Entert the filename')
word = input('Enter the word') #which word count you need
wordcount(filename,word)


# In[5]:


#character count from the given file
def charcount(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x=f.read()
            li=list(x) #converting the string-charcount
    return len(li)
filename = input('enter the filename :')
charcount(filename)


# In[9]:


#function to print the upper and lower characters
def casecount(filename):
    cntupper=0
    cntlower=0
    with open(filename,'r') as f:
        if f.mode == 'r':
            x=f.read()
            li=list(x)
    for i in li:
        if i.isupper():
            cntupper=cntupper+1
        if i.islower():
            cntlower=cntlower+1
    output='Uppercase={0},Lowercase={1}'.format(cntupper,cntlower)
    return output
filename=input("Enter filename")
casecount(filename)
                    


# In[11]:


def countline(filename):
    with open(filename,"r") as f :
        if f.mode =='r':
            x=f.read()
            li=x.split("\n")
    return len(li)
filename=input("Enter the filename :")
countline(filename)


# # math ,random,os
# 
# ##  . os package it contains the certain kind of methods with works with os

# In[13]:


pwd


# In[16]:


cd Desktop


# In[17]:


cd pythonprogramming


# In[18]:


cd Git


# In[19]:


cd ..


# In[20]:


dirpath ='Git/'
with os.scandir(dirpath) as f:
    for i in f:
        if i.is_file():
            print(i.name)


# In[ ]:





# In[ ]:




