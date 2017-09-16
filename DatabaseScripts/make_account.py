#!/usr/bin/python

# connects to Accounts database
import pymysql
accGetter = pymysql.connect(
    db='Accounts',
    user='root',
    passwd='root',
    host='localhost')
account=acc.cursor()
account.execute("INSERT INTO Account_Mapping VALUES (Null, 0)")
accGetter.commit()

account.execute("SELECT MAX(user_id) FROM Account_Mapping")
print("Your user id is:")
print([(r[0]) for r in account.fetchall()])
print("Make sure to copy and paste this user id when uploading stuff!")
