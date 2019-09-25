import mysql.connector
import os
import sys
import logging

from Logging1 import *


class Menu:
    def Readfile(self):
        self.db = mysql.connector.connect(host="localhost", user="root", passwd="user123",database="MENU")
        self.cursor = self.db.cursor()
        #self.cursor.execute("CREATE DATABASE MENU")

        #self.cursor.execute("CREATE TABLE menu_data(name VARCHAR(255))")

    def select(self,a):

        obj=Menu()
        obj.Readfile()
        self.query = "SELECT * FROM menu WHERE name=%s"
        self.cursor.execute(self.query,(a[1],))
        self.data = self.cursor.fetchall()
        self.l1=list()
        for data in self.data:
            self.s1=''.join(data)
            self.l1.append(self.s1)
        print(self.l1)


    def update(self,a):
      if(a[1]=="update"):
        obj=Menu()
        obj.Readfile()
        self.col_name=(a[2])
        self.query1="INSERT INTO menu_data(name) VALUES(%s) "
        self.values=[(a[2])]
        self.cursor.execute(self.query1,self.values)
        self.q1 = "CREATE TABLE " + self.col_name + "(name varchar(255),price varchar(5))"
        self.cursor.execute(self.q1)
        self.query3 = "INSERT INTO " + self.col_name + "(name,price) VALUES(%s,%s)"
        self.l1 = a[3].split(",")
        #print(self.l1)
        self.values = list()
        self.i = 0
        for j in range(self.i, len(self.l1)):
            self.l2 = self.l1[j].split(":")
            self.values.append(tuple(self.l2))


        self.cursor.executemany(self.query3, self.values)
        self.db.commit()
        print("Data Updated..Check in Menu Database...")



    def delete(self,a):
      if(a[1]=="delete"):
        obj=Menu()
        obj.Readfile()

        self.query="DELETE FROM menu_data WHERE name=%s"
        self.cursor.execute(self.query,(a[2],))
        self.query1="DROP TABLE "+ a[2]
        self.cursor.execute(self.query1)
        self.db.commit()
        print("Data Deleted...Check Menu Database..")
        #obj.select()

    def menu_display(self):
        obj = Menu()
        obj.Readfile()
        log = Logging1()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # filehandler_obj.setLevel('WARNING')
        logging.info("Menu.py.....")
        print("Welcome to the Menu.py...")
        print("-------------------------------")

        self.query3 = "SELECT * FROM menu_data"
        self.cursor.execute(self.query3)
        self.data = self.cursor.fetchall()
        # print(self.records)
        self.l1 = list()
        for data in self.data:
            self.s1 = ''.join(data)
            self.l1.append(self.s1)
        print("Menu: ",self.l1)
        print("Write 'Exit' for back to Main Menu")
        t = input("Enter Main Item name:")

        while(t!="Exit"):
            if(t in self.l1):
                self.q1="SELECT name FROM " + t
                self.cursor.execute(self.q1)
                self.data=self.cursor.fetchall()
                self.l2 = list()
                for data in self.data:
                    self.s1 = ''.join(data)
                    self.l2.append(self.s1)
                print("-----------------------------------------------------------")
                print(t +" type: ", self.l2)
                print("-----------------------------------------------------------")
                print("Menu: ", self.l1)  # display Main Menu.
                print("Write 'Exit' for back to Main Menu")
                t = input("Enter Main Item name: ")
            else:
                log = Logging1()
                logger = logging.getLogger()
                logger.setLevel(logging.WARNING)
                #filehandler_obj.setLevel('WARNING')
                logging.warning("Enter Wrong item name...: " + t)
                print("Enter Wrong Item name..")
                t = input("Enter Main Item name: ")

        while (t == "Exit"):
            print("---------------------------------------------")
            print("Pls Write 'Cart select' to place the order..")
            print("----------------------------------------------")
            break


obj=Menu()
obj.Readfile()

obj.update(sys.argv)
obj.delete(sys.argv)
#obj.select(sys.argv)
#obj.menu_display()
