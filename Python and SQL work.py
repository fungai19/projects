#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandasql import sqldf


# In[2]:


#define a lambda q: sqldf(q,globals())


# In[3]:


pysqldf = lambda q: sqldf(q, globals())


# In[4]:


#IMPORT DATA
employees = pd.read_excel("/Users/fez/Desktop/DAIB/LAB 7 – Data sets-20220221/EmployeesData.xlsx")


# In[5]:


#Import orders data - Matt G, Jason T, Matt W, and 
#La Shanda H go to sushi lunch taking a potential client with them

orders = pd.read_excel("/Users/fez/Desktop/DAIB/LAB 7 – Data sets-20220221/OrdersData.xlsx")


# In[6]:


male_employees = pysqldf("SELECT * FROM employees WHERE gender = 'm'")
#print(male_employees)


# 

# In[7]:


name_counts = pysqldf("""SELECT firstname,
                         COUNT (firstname) as occurances
                         FROM employees
                         GROUP BY firstname""")
print(name_counts)


# In[8]:


name_counts_employ = pysqldf("""SELECT firstname,
                                COUNT(firstname) as occurances
                                FROM employees
                                WHERE firstname != 'rudi'
                                GROUP BY firstname""")
print(name_counts_employ)


# In[9]:


employees_cali = pysqldf(""" SELECT *,
                        CASE
                            WHEN lower(firstname)= 'stewart' THEN 1
                            WHEN lower(firstname) = 'jila' THEN 1
                            WHEN lower(firstname) = 'jon' THEN 1
                            WHEN lower(firstname) = 'solon' THEN 1
                            ELSE 0
                            END as cali_emp
                            FROM employees
                            """)
print(employees_cali)


# In[10]:


employees_cali_sorted = pysqldf("""SELECT *,
 CASE
 WHEN lower(firstname) = 'stewart' THEN 1
 WHEN lower(firstname) = 'hila' THEN 1
 WHEN lower(firstname) = 'jon' THEN 1
 WHEN lower(firstname) = 'solon' THEN 1
 ELSE 0
 END as cali_emp
 FROM employees
 ORDER BY cali_emp DESC, firstname
 """)
print(employees_cali_sorted)


# # Practicing multi-table operations

# In[11]:


left_join = pysqldf("""SELECT *
                       FROM employees
                       LEFT JOIN orders 
                       ON employees.id=orders.id
                       WHERE employees.firstname != 'rudi'
                       """)
print(left_join)


# In[12]:


right_join_equiv = pysqldf("""SELECT *
                           FROM orders
                           LEFT JOIN employees
                           ON employees.id=orders.id
                           """)
print(right_join_equiv)


# In[13]:


q = "SELECT name FROM sqlite_master WHERE type = 'table'"

tables = pd.read_sql_query(q, con)

tables


# In[14]:


q = "select * from tracks"
t = pd.read_sql_query(q, con)
t


# In[ ]:




