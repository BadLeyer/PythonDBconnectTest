# -*- coding: utf-8 -*-
 
from db import CvDB

def newPw():

    db = CvDB()


    print('新しい名前を入力')
    newName = raw_input()
    print('現在の名前を入力')
    name2 = raw_input()
    print('現在のパスワードを入力')
    now_pw = raw_input()
    db.nameUpdate(newName,name2,now_pw)
