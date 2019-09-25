import os
import sys
import mysql.connector
import logging

from Logging1 import *




class Welcome:

    def Readfile(self):
        self.db=mysql.connector.connect(host="localhost",user="root",passwd="user123",database="MENU")
        self.cursor=self.db.cursor()

        #self.q1="CREATE TABLE Login(user_name varchar(20) NOT NULL,password varchar(10) NOT NULL)"
        #self.cursor.execute(self.q1)
    def user_check(self):
        obj=Welcome()
        obj.Readfile()
        self.t3=input("Registered User? ")
        if(self.t3=="Yes"):
            self.t1=input("Enter Username: ")
            self.t2=input("Enter Password: ")

            self.q3 = "SELECT * FROM Login "
            self.cursor.execute(self.q3)
            self.data = self.cursor.fetchall()
            # print(self.records)
            self.l1 = list()
            for data in self.data:
               self.s1 = ''.join(data[0:1])
               self.s2 = ''.join(data[1:])
               self.l1.append([self.s1,self.s2])
            print(self.l1)
            self.a=0
            for element in self.l1:
               self.a=self.a+1
               if(self.t1==element[0] and self.t2== element[1] ):
                   log = Logging1()
                   logger = logging.getLogger()
                   logger.setLevel(logging.INFO)
                   # filehandler_obj.setLevel('WARNING')
                   logging.info("Welcome.py.....")
                   print("Welcome to the foody.py.....")
                   print("----------------------------------------------")
                   self.q7="CREATE TABLE REST_NAME(name VARCHAR(20))"
                  # self.cursor.execute(self.q7)
                   self.q8="INSERT INTO REST_NAME(name) VALUES(%s)"
                   self.values=(["ShivShakti"],["Udupi"],["MoochMarod"],["Ashirwad"])
                   #self.cursor.executemany(self.q8,self.values)
                   self.db.commit()

                   self.q9="SELECT * FROM REST_NAME"
                   self.cursor.execute(self.q9)
                   self.data3=self.cursor.fetchall()
                   self.l1=list()
                   for data in self.data3:
                       self.s3=''.join(data)
                       self.l1.append(self.s3)
                   print("Restaurant: ",self.l1)
                   print()
                   self.t7=input("Select Restaurant: ")
                   print()
                   print("Write 'Menu' to see the Menu..")
                   self.q5 = "CREATE TABLE Orderplaced(No VARCHAR(20),OrderNo VARCHAR(20), Cust_Name VARCHAR(20),Rest_Name VARCHAR(20))"
                   #self.cursor.execute(self.q5)
                   self.q4 = "SELECT * FROM Orderplaced "
                   self.cursor.execute(self.q4)
                   self.data1 = self.cursor.fetchall()
                   # print(self.records)
                   if (len(self.data1) == 0):
                       self.q2 = "INSERT INTO Orderplaced(No,OrderNo,Cust_Name,Rest_Name) VALUES(%s,%s,%s,%s)"
                       self.values = ("1", "order1", self.t1,self.t7)
                       self.cursor.execute(self.q2, self.values)
                       self.q6 = "CREATE TABLE order1 (name VARCHAR(255),quantity VARCHAR(255),price VARCHAR(255))"
                       self.cursor.execute(self.q6)
                       self.db.commit()
                   else:
                       for data in self.data1:
                           self.s1 = ''.join(data[0:1])

                       self.q2 = "INSERT INTO Orderplaced(No,OrderNo,Cust_Name,Rest_Name) VALUES(%s,%s,%s,%s)"
                       self.c = (int(self.s1)) + 1
                       self.o = "order" + str(self.c)
                       self.values = (str(self.c), self.o, self.t1,self.t7)
                       self.cursor.execute(self.q2, self.values)

                       self.q6 = "CREATE TABLE " + self.o + " (name VARCHAR(255),quantity VARCHAR(255),price VARCHAR(255))"
                       self.cursor.execute(self.q6)
                       self.db.commit()

                   break

               else:
                   if((self.a==len(self.l1))):
                       log = Logging1()
                       logger = logging.getLogger()
                       logger.setLevel(logging.WARNING)
                       #filehandler_obj.setLevel('WARNING')
                       logging.warning("Incorect Username and  password...: " + self.t1+" "+self.t2)
                       print("Enter Correct Username and Password...")


        else:
            self.t4 = input("Registered First..")
            self.t1 = input("Enter Username: ")
            self.t2 = input("Enter Password: ")
            self.q4 = "SELECT * FROM Login "
            self.cursor.execute(self.q4)
            self.data1 = self.cursor.fetchall()
            # print(self.records)
            if(len(self.data1)==0):
                self.q2 = "INSERT INTO Login(user_name,password) VALUES(%s,%s)"
                self.values = [self.t1, self.t2]
                self.cursor.execute(self.q2, self.values)
                print("U R Sucessfully Registered...")
                print("Pls Login... ")
                self.db.commit()
            else:
                self.l2 = list()
                for data in self.data1:
                    self.s1 = ''.join(data[0:1])
                    self.s2 = ''.join(data[1:])
                    self.l2.append([self.s1, self.s2])
                # print(self.l1)
                self.a=0
                for element in self.l2:
                    self.a=self.a+1;
                    if (self.t1==element[0]):
                        print("Username already registered. Use another Username ")
                        break

                    if(self.a==len(self.l2)):

                        self.q2 = "INSERT INTO Login(user_name,password) VALUES(%s,%s)"
                        self.values = [self.t1, self.t2]
                        self.cursor.execute(self.q2, self.values)
                        print("U R Sucessfully Registered...")
                        print("Pls Login... ")
                        self.db.commit()

obj2=Welcome()
obj2.Readfile()
