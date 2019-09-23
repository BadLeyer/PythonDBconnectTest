# -*- coding: utf-8 -*-
import sqlite3
from model import *
from db import CvDB





def main():
    print ("名前を入力してください")
    userName = raw_input()
    print ("パスワードを入力してください")
    userPw = raw_input()

    """dbから取得したテーブルをレコード（リスト）に変換"""
    db = CvDB()
    login = db.selectUsers(userName,userPw)
    for l in login:
        print(l)

    if l[0] == userName and l[1] == userPw:
        print ('認証成功')
    else :
        print ('認証失敗もう一度名前を入力してください')
        re_userName = raw_input()
        print('パスワードを入力してください')
        re_userPw = raw_input()


        rere_userName = None
        rere_userPw = None
        """ログイン失敗用のループ"""
        while re_userName != l[0] and re_userPw != l[1] or rere_userName != l[0] and rere_userPw != l[1]:
            
            print ('認証失敗もう一度名前を入力してください')
            rere_userName = raw_input()

            print('パスワードを入力してください')
            rere_userPw = raw_input()

        print('認証成功')
        
    """
    num1 = raw_input()
    if num1 == '1':
        print('①を実行します')
    elif num1 == '2':
        print('②を実行します')
    elif num1 == '3':
        print('③を実行します')
    elif num1 == '0':
        print('終了します')
    else :
        print('有効な数字を入力してください')
        """
    flag = True
    num2 = None

    while flag == True:
        print('①の場合は１を②の場合は２を、③の場合は３を、終了の場合は０を押してください')
        num2 = raw_input()
        if num2 == '1':
            newPw()
        elif num2 == '2':
            print('②を実行します')
        elif num2 == '3':
            print('③を実行します')
        elif num2 == '0':
            flag = False
            print('終了します')
        else :
            print('もう一度')
            print(num2)
        
            

        



        #db = CvDB()
    #db.insertName('sasebo','aaa')
    #rows = db.selectName('aa')押してください
    #for r in rows:
     #   print(r)
if __name__ == '__main__':
    main()