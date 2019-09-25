import os
import sys
import mysql.connector
import logging
from Payment import *
from Logging1 import *
from Welcome import *

class Order:
    def Read_file(self):
      self.db = mysql.connector.connect(host="localhost", user="root", passwd="user123", database="MENU")
      self.cursor = self.db.cursor()


    def order_display(self,a):
      if(a[2]=="display"):

        self.q1="SELECT * FROM Ordercode"
        self.cursor.execute(self.q1)
        self.data = self.cursor.fetchall()  # it's in a tuple into list form. eg.self.data= [("1234")]

        self.l1 = list()

        for data in self.data:  # first tuple of list
            self.s1 = ''.join(data[0:1])  # ''.join()convert tuple into string.eg. ("Gobi")=Gobi
            self.s2=''.join(data[1:2])

        while(self.s1):

            log=Logging1()
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            #filehandler_obj.setLevel('INFO')
            logging.info("Order done...")

            print("U r order is Confirmed..")
            print("U r order code is:",self.s1 +"  and OrderNo is: ",self.s2)
            print("It takes some processing time..")
            print("Thank you..")
            #self.q2="DELETE FROM " + self.o
            #self.cursor.execute(self.q2)
            #self.q3 = "DELETE FROM Ordercode1"
            #self.cursor.execute(self.q3)
            self.db.commit()
            break
        else:
            print("Pls pay the bill First...")
    def cancelorder(self,a):
        if(a[2]=="cancelorder"):
            print("U r order is cancelled..")
            print("Amount is Refunded in 3-4 business days...")