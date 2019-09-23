# -*- coding: utf-8 -*-
import sqlite3

class CvDB:

    def __init__(self):
        self.dbName = 'CV.sqlite'

    def insertName(self,id,pw):
        #conn = mysql.connector.connect(host=self.host,user=self.user,password=self.pw,database=self.database)
        conn = sqlite3.connect(self.dbName)
        cur = conn.cursor()
        try:
            data =[(id,pw)]
            cur.execute("INSERT INTO users(use_pw,sign_up_time,use_names,use_now) values('11','2010/10/10 10:10:10',?,?)",data)
            conn.commit()
        except:
            conn.rollback()
            print('失敗')
        finally:
            conn.close()

    def selectName(self,name):
        conn = sqlite3.connect(self.dbName)
        cur = conn.cursor()
        result = ""
        try :
            data = [(name)]
            cur.execute("select * from users")
            result= conn.fetchall()
        except :
            conn.rollback()
            print('失敗1')
        finally :
            conn.close()
        return result

    """ログイン用情報　名前　パスワード"""
    def selectUsers(self,name,pw):
        conn = sqlite3.connect(self.dbName)
        cur = conn.cursor()
        result = "NULL"

        try :
            data = [(name,pw)]
            cur.execute("select use_names,use_pw from users")
            result = cur.fetchall()
        except sqlite3.Error as e:
            conn.rollback()
            print(args[0])
            print('失敗３')


        finally :
            conn.close()
        return result

    """ユーザー情報を変更"""
    def nameUpdate(self,name2,pw,newName):
        conn = sqlite3.connect(self.dbName)
        cur = conn.cursor()
        result = "NULL2"

        try:
            data= [(newName,name,pw)]
            cur.execute("update users set use_names = ? where use_names = ? and use_pw = ?")
            conn.commit()
            print('成功')
        except sqlite3.Error as e:
            conn.rollback()
            print("失敗４")
        
        finally :
            conn.close()
        return result