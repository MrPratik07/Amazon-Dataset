#!/usr/bin/env python
# coding: utf-8

# # Jobs available in Banglore and Seattle

# In[4]:


import csv
count1=0
count2=0
with open('Datasets/amazon_jobs_dataset.csv','r',encoding="utf8") as file_obj:
    file_data=csv.reader(file_obj,skipinitialspace=True)
    file_list=list(file_data)
location=[]
for row in file_list[1:]:
    value=row[2]
    if 'Bangalore' in value:
        count1+=1
    elif 'Seattle' in value:
        count2+=1
print("Jobs in banglore",count1)
print("Jobs in Seattle",count2)


# # Jobs available as a Computer Vision

# In[6]:


import csv
count1=0
with open('Datasets/amazon_jobs_dataset.csv','r',encoding="utf8") as file_obj:
    file_data=csv.reader(file_obj,skipinitialspace=True)
    file_list=list(file_data)
jobs=[]
for row in file_list[1:]:
    value=row[1]
    if 'Computer Vision' in value:
        count1+=1
print("jobs in Computer Vision",count1)        
    


# # jobs available in Canada

# In[3]:


import csv
count1=0
with open('Datasets/amazon_jobs_dataset.csv','r',encoding="utf8") as file_obj:
    file_data=csv.reader(file_obj,skipinitialspace=True)
    file_list=list(file_data)
jobs=[]
for row in file_list[1:]:
    value=row[2].split(",")
    if(value[0]=='CA') :  
        count1+=1
print("jobs in canada are",count1)             
    


# # Highest no of job openings in month

# In[9]:


import csv
count1=0
with open('Datasets/amazon_jobs_dataset.csv','r',encoding="utf8") as file_obj:
    file_data=csv.reader(file_obj,skipinitialspace=True)
    file_list=list(file_data)
dict={}
for row in file_list[1:]:
    value=row[3].split(",")
    if(value[1].strip()=='2018'):
        value2 = value[0].split(' ')
        month = value2[0].strip()
        if month in dict:
            dict[month] += 1
        else:
            dict[month] = 1
v = list(dict.values()) 
k = list(dict.keys())  
print("The no of jobs openings are in month",k[v.index(max(v))],"with no of openings",max(v)) 


# # No of jobs available for Bachelors degree

# In[2]:


import csv
with open('Datasets/amazon_jobs_dataset.csv','r',encoding="utf8") as file_obj:
    file_data=csv.reader(file_obj,skipinitialspace=True)
    file_list=list(file_data) 
count=0
for row in file_list[1:]:
    #p=row['BASIC QUALIFICATIONS']
    p=row[5]
    if "Bachelor" in p:
        count+=1
    elif "BS" in p:
        count+=1
    elif "BA" in p:
        count+=1
print("No of jobs available for bachelors degree is",count)


# # Among Java, C++ and Python, which of the language has more job openings in India for Bachelor Degree Holder?

# In[5]:


## Open and read data file as specified in the question
## Print the required output in given format
import csv
with open('Datasets/amazon_jobs_dataset.csv','r',encoding="utf8") as file_obj:
    file_data=csv.reader(file_obj,skipinitialspace=True)
    file_list=list(file_data) 
count=0
count1=0
count2=0

for row in file_list[1:]:
   if row[2][:2] == 'IN':
       p=row[5]
       if "Bachelor" in p or  "BS" in p or "BA" in  p:
            if "Java" in p:
                count+=1
                if "C++" in p:
                    count1+=1
                    if "Python" in p:
                        count2+=1
ans = max(count, max(count1, count2))
if ans == count:
     print('Java', ans)
elif ans == count1:
     print('C++', ans)
else:
     print('Python', ans)


# # Most No of Java developers openings in Country

# In[2]:


## Open and read data file as specified in the question
## Print the required output in given format

import csv
path='Datasets/amazon_jobs_dataset.csv'
country_basic_qualifications=[]
with open(path,'r',encoding='utf-8') as csvFile:
    reader=csv.DictReader(csvFile)
    for row in reader:
        country_basic_qualifications.append([row['location'],row['BASIC QUALIFICATIONS']])
## Get Java Developer from the different country
def getTheJavaDeveloper(arr):
    arrlist=[]
    for i in arr:
        if 'Java' in i[1]:
            arrlist.append(i[0].split(',')[0])
    return arrlist
java_developer=getTheJavaDeveloper(country_basic_qualifications)
def createDictionary(arr):
    dictionary={i:0 for i in set(arr)}
    for i in arr:
        dictionary[i]=dictionary.get(i)+1
    return dictionary
def convertDictToList(dictionary):
    arrlist=[]
    for i in dictionary:
        arrlist.append([dictionary.get(i),i])
    arrlist.sort(reverse=True)
    return arrlist
java_dict=createDictionary(java_developer)
java_list=convertDictToList(java_dict)
print(java_list[0][1],java_list[0][0])


# In[ ]:




