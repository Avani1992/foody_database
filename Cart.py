import os
import sys
import mysql.connector
import  logging

from Logging1 import *


class Cart:
    def Read_file(self):
        self.db = mysql.connector.connect(host="localhost", user="root", passwd="user123", database="MENU")
        self.cursor = self.db.cursor()

        #self.cursor.execute("CREATE TABLE Order(name VARCHAR(255),quantity VARCHAR(255))")
        #self.db.commit()


    def select(self,a):   # To place the order..
      if(a[2]=="select"):
        log = Logging1()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # filehandler_obj.setLevel('WARNING')
        logging.info("Cart select.....")

        print("Welcome to Cart.py...")
        print("------------------------")

        self.query3 = "SELECT * FROM menu_data"
        self.cursor.execute(self.query3)
        self.data = self.cursor.fetchall()        # store tuple data in list form. eg. [("Roti",),("Sabji",)]
        # print(self.records)
        self.l1 = list()
        for data in self.data:
            self.s1 = ''.join(data)  # convert tuple data into string
            self.l1.append(self.s1)
        print("Menu: ",self.l1)                  # Print the Menu
        print("Write 'Exit'' for back to main menu...")
        t = input("Enter Item name:")              # Ask for choice

        #self.d = dict()
        self.item = list()
        self.value = list()
        self.price=list()
        while (t != "Exit"):                # until user write Exit

            if(t in self.l1):             # If choice of user is in l1 eg. Roti
                self.q1 = "SELECT name FROM " + t
                self.cursor.execute(self.q1)
                self.data = self.cursor.fetchall()
                self.l2 = list()
                for data in self.data:
                    self.s1 = ''.join(data)
                    self.l2.append(self.s1)
                print(t + " type: ", self.l2)

                t1 = input(t + " type(e.g : write name of Item):")    # Ask type of that data eg. if user write 1. so itmeans Plain roti
                self.q2="SELECT price FROM " + t +" WHERE name=%s"
                self.cursor.execute(self.q2,(t1,))
                self.data1 = self.cursor.fetchall()

                for data in self.data1:
                    self.s3 = ''.join(data)
                    self.price.append(self.s3)

                self.item.append(t1) # Write the name of data. eg. self.data["Roti"]["1"]=Plain
                #print(self.item)
                t2=input("Quantity of " + t+" :")
                self.value.append(t2)
                #print(self.value)

                #self.data1[self.s1] = self.s2  # Add data in Dictionarty eg. Plain:2
                print("----------------------------------------")
                print("Menu: ",self.l1)
                print("Write 'Exit'' for back to main menu...")
                t = input("Enter Item name:")
            else:
                log = Logging1()
                logger = logging.getLogger()
                logger.setLevel(logging.WARNING)
                #filehandler_obj.setLevel('WARNING')
                logging.warning("Enter Wrong item name...: " + t)
                print("Enter Wrong Item name..")
                t = input("Enter  Item name: ")



        if (t == "Exit"):
            self.q1="SELECT OrderNo FROM Orderplaced"
            self.cursor.execute(self.q1)
            self.data2=self.cursor.fetchall()
            for data in self.data2:
                self.s1=''.join(data)

            self.q3="INSERT INTO " + self.s1 + "(name,quantity,price) VALUES (%s,%s,%s)"
            for i in range(0,len(self.item)):
                j=i
                self.values=[self.item[i],self.value[j],str((int(self.price[j])) *10)]
                self.cursor.execute(self.q3,self.values)
            self.db.commit()
            print("---------------------------------------------")
            print("Pls Write 'Cart display' to see the order..")
            print("----------------------------------------------")

    def cart_display(self,a):           # to display the order which is place by the user...

      if(a[2]=="display"):
          log = Logging1()
          logger = logging.getLogger()
          logger.setLevel(logging.INFO)
          # filehandler_obj.setLevel('WARNING')
          logging.info("Cart display.....")
          self.q1 = "SELECT OrderNo FROM Orderplaced"
          self.cursor.execute(self.q1)
          self.data2 = self.cursor.fetchall()
          for data in self.data2:
              self.s1 = ''.join(data)
          print("U r order: ")
          print("------------ ")
          self.query="SELECT * FROM " + self.s1
          self.cursor.execute(self.query)
          self.data = self.cursor.fetchall()   # it's in a tuple into list form. eg.self.data= [("Gobi","1"),("Plain","3")]
          self.l1 = list()
          for data in self.data:  # first tuple of list
            self.s2 = ''.join(data[0:1])  # ''.join()convert tuple into string.eg. ("Gobi")=Gobi
            self.s3=''.join(data[1:2])

            print(self.s2+"  "+self.s3)

          print("---------------------------------------------")
          print("Pls Write 'Payment displaybill' to see  the TotalBill..")
          print("----------------------------------------------")


obj=Cart()
obj.Read_file()