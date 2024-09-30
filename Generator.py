import random
import pandas as pd
import numpy as np

def list(file):

    # open file with names
    with open(file) as fp:
        new_list = []
        # loop through each line in the txt file 
        for line in fp:
            
            new_list.append(line.strip())
    return new_list

# call the function three times to transform names from each
# file into arrays 
file = "data/Publisher.txt"
publisher = list(file)

file = "data/Book-Title.txt"
title = list(file)

file = "data/Book-Author.txt"
author = list(file)


min=1970
max=2005
nbr_users=2000
data_size=2000
nbr_queries=2000

def random_profile():
    year_of_publication = random.randint(min, max)
    # randomly choose a profile
    item = [random.choice(publisher),year_of_publication,random.choice(title), random.choice(author)]
    return item

data=[]


for i in range(data_size):
  data.append(random_profile())




datadf=pd.DataFrame(data,columns=["Publisher", "Year-Of-Publication","Book-Title","Book-Author"])
datadf.to_csv('./csv/dataset.csv',index=False)

print("Dataset created ")

##########################
users = []
for i in range(nbr_users):
		user = "U" + str(i+1)
		users.append(user)

usersdf=pd.DataFrame(users,columns=['Used_Id'])
usersdf.to_csv("./csv/users.csv",index=False)

print("Users set created ")

####################################################################################
queries=[]
d=0
while d < nbr_queries:
    
    queryID = "Q" + str(d + 1)
    query = ''
    
    if random.randint(0, 1) == 1:#try to pick name for query
      if len(query)>0: query+=','
      query+=('Publisher=' + random.choice(publisher))
    if random.randint(0, 1) == 1:
      if len(query)>0: query+=','
      query+=('Book-Title=' + random.choice(title))
    if random.randint(0, 1) == 1:
      if len(query)>0: query+=','
      query+=('Year-Of-Publication=' + str(random.randint(1970, 2005)))
    if random.randint(0, 1) == 1:
      if len(query)>0: query+=','
      query+=('Book-Author=' + random.choice(author))

    if len(query)>0:
      queries.append({"queryID":queryID,"query":query})
      d+=1

queries=pd.DataFrame(queries, columns =['queryID','query'])
queries.to_csv('./csv/queries.csv',index=False)

print("Queries set created ")

