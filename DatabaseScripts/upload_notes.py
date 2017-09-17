#!/usr/bin/python
import pymysql

# connect to "Images" database
accGetter = pymysql.connect(
    db='Accounts',
    user='root',
    passwd='root',
    host='localhost')
account=accGetter.cursor()

# This will get values from the input boxes later
user_id=1
link="bigrednotes.azurewebsites.net/library/"+user_id+"_"+name
name="image"
vote_num=0
download_num=0
tag="List"
school_class="Memology"

# Inputs values into repo
account.execute("INSERT INTO Images VALUES (user_id,link,name,vote_num,download_num,tag,school_class)")
accGetter.commit()
print("Successfully uploaded!")
