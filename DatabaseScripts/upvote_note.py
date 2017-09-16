#!/usr/bin/python
import pymysql

# connect to "Images" database
accGetter = pymysql.connect(
    db='Accounts',
    user='root',
    passwd='root',
    host='localhost')
account=accGetter.cursor()
linkn=""

account.execute("UPDATE Images SET vote_num=vote_num+1 WHERE (link=linkn)")
accGetter.commit()
