#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import pymysql

class DB(object):
    def __init__(self):
        db = pymysql.connect(host="localhost", user="root",password="175150", db="roll", port=3306)
        cur = db.cursor()
        self.cur=cur
        self.connection=db

    def process_item(self, item):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, dict):
            # if self.data.find_one({"nickname":item["nickname"],"Post":item["Post"],"Pubtime":item["Pubtime"]}):
            #      return "null"
            # else:
                # self.data.insert(item)
              self.cur.execute(
                "insert into roll(newslabels, title_alls, newstimes, post) values(%s, %s, %s, %s)",
                (item["newslabels"], item["title_alls"], item["newstimes"], item["post"]
                 ,))
              self.connection.commit()
              print("insert data into database...")
              return "ok"

    def get_Post():
        cnxn = pymysql.connect(host="localhost", user="root", password="175150", db="roll", port=3306)
        cur = cnxn.cursor()
        select = "Select post from roll"
        cur.execute(select)
        row = cur.fetchall()
        # row = cur.fetchone()
        if row:
            return row
        else:
            # raise Exception, "There seems no operator on sector:" + str(sectorNumber)
            print("There seems no Post")
        cnxn.close()


