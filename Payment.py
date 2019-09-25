import os
import sys
import mysql.connector
import logging

from Cart import *
from Logging1 import *


class Payment:
    def Read_file(self):
        self.db = mysql.connector.connect(host="localhost", user="root", passwd="user123", database="MENU")
        self.cursor = self.db.cursor()

    def payment_display(self,a):

        if(a[2]=="displaybill"):
            log = Logging1()
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            # filehandler_obj.setLevel('WARNING')
            logging.info("Payment displaybill.....")
            print("Welcome to Payment.py..")
            print("---------------------------")
            print("Item" + "      " + " Quantity"+"    "+"Price"+"    "+"Total")
            print("-------------------------------------")
            self.q1 = "SELECT OrderNo FROM Orderplaced"
            self.cursor.execute(self.q1)
            self.data2 = self.cursor.fetchall()
            for data in self.data2:
                self.s7 = ''.join(data)

            self.query = "SELECT * FROM " + self.s7
            self.cursor.execute(self.query)
            self.data = self.cursor.fetchall()  # it's in a tuple into list form. eg.self.data= [("Gobi","1"),("Plain","3")]

            self.l1 = list()
            self.sum=0
            for data in self.data:  # first tuple of list
                self.s1 = ''.join(data[0:1])  # ''.join()convert tuple into string.eg. ("Gobi")=Gobi
                self.s2 = ''.join(data[1:2])
                self.s3=''.join(data[2:])
                self.s4=(int(self.s2) * int(self.s3))
                print(self.s1 + "    " + self.s2 +"     "+(self.s3)+"   "+str(self.s4))
                self.sum=self.sum+self.s4
            print("--------------------------------")
            print("Total Amount is:", self.sum)
            if (self.sum == 0):
                print("Pls Place the order")
            else:
                print("For Payment Write 'paybill' ")
                print("For update(Add/Delete) items Write 'updateorder' ")


    def updateorder(self,a):
        if(a[2]=="updateorder"):
            log = Logging1()
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            # filehandler_obj.setLevel('WARNING')
            logging.info("Updateorder.....")
            t=input("Do u want to change the order(Yes/No): ")
            if(t=="Yes"):
                t1=input("Do u want to add some items(Yes/No)?: ")
                if(t1=="Yes"):
                    print("Add items from Cart select")
                    obj=Cart()
                    obj.Read_file()             # If user wants to add item in oreder back to the cart for display menu and add item in cart.
                    obj.select(sys.argv)
                    obj1=Payment()
                    obj1.Read_file()
                    obj1.payment_display(sys.argv)      # After adding item in cart further ask for payment option

                elif(t1=="No"):
                    t1=input("R u want to delete some items(Yes/No)?:")
                    if(t1=="Yes"):

                        print(" U r Order:")
                        print("---------------")
                        self.q1 = "SELECT OrderNo FROM Orderplaced"
                        self.cursor.execute(self.q1)
                        self.data2 = self.cursor.fetchall()
                        for data in self.data2:
                            self.s7 = ''.join(data)
                        self.query = "SELECT * FROM "+self.s7
                        self.cursor.execute(self.query)
                        self.data = self.cursor.fetchall()  # it's in a tuple into list form. eg.self.data= [("Gobi","1"),("Plain","3")]
                        self.l1 = list()
                        for data in self.data:  # first tuple of list
                            self.s1 = ''.join(data[0:1])  # ''.join()convert tuple into string.eg. ("Gobi")=Gobi
                            self.s2 = ''.join(data[1:2])

                            print(self.s1 + "  " + self.s2)
                        print("------------------------")
                        t2=input("Enter item name which u want to delete:")
                        #if(t2 in self.data):            # check if the item is in data which user wants to delete
                        self.q1="DELETE FROM "+ self.s7 +" WHERE name=%s"      # If it is delete it from data
                        self.cursor.execute(self.q1,(t2,))
                        self.db.commit()

                        print(" U r order is Updated.check it in Payment displaybill.. ")


    def Bill_pay(self,a):
     if(a[2]=="paybill"):
        log = Logging1()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # filehandler_obj.setLevel('WARNING')
        logging.info("Payment billpay.....")
        print("Payment Mode:")
        self.d=dict()
        self.d[1]="Paytm"
        self.d[2]="NetBanking"
        self.d[3]="Creditcard"
        self.d[4]="Debitcard"
        print(self.d)
        t=input("Enter Payment Mode:")
        if(t=='1'):
            t=input("Enter u r Paytm four digit code:")
            while(str(len(t))):
              if(str(len(t))==str(4)):

                self.payment="Done"
                self.ordercode="1234"
                print("------------------------------")
                print("U r payment is Done..")
                break
              else:
                log = Logging1()
                logger = logging.getLogger()
                logger.setLevel(logging.WARNING)
                #filehandler_obj.setLevel('WARNING')
                logging.warning("Incorect pin...: " +t)
                print("Enter Correct Pin..")
                print("")
                t = input("Enter u r Paytm four digit code:")
        elif(t=='2'):
            print("Enter u r NetBanking Details:")
            t=input("Username: ")
            t1=input("Password: ")
            while (str(len(t1))):
             if(str(len(t1))==str(4)):
                self.payment="Done"
                self.ordercode="4567"
                print("")
                print("U r payment is Done..")
                break
             else:
                log = Logging1()
                logger = logging.getLogger()
                logger.setLevel(logging.WARNING)
                #filehandler_obj.setLevel('WARNING')
                logging.warning("Incorrect password...:" + t1)
                print("Enter Correct Password:")
                print("")
                t1=input("Password: ")
        elif(t=='3' or t=='4'):
            t=input("Enter Card Details:")
            t2=input("Enter 3 digit pin:")
            while (str(len(t2))):
             if(str(len(t2))==str(3)):
                self.payment="Done"
                self.ordercode="6789"
                print("")
                print("U r payment is Done..")
                break
             else:
                log = Logging1()
                logger = logging.getLogger()
                logger.setLevel(logging.WARNING)
                #filehandler_obj.setLevel('WARNING')
                logging.warning("Incorect pin...:" + t2)
                print("Enter Correct Pin..")
                print("")
                t2=input("Enter 3 digit pin: ")
        while(self.payment=="Done"):
            self.q = "SELECT * FROM Orderplaced"
            self.cursor.execute(self.q)
            self.data2 = self.cursor.fetchall()
            for data in self.data2:
                self.s7 = ''.join(data[1:2])
                self.s8=''.join(data[2:3])
                self.s9=''.join(data[3:])

            self.q1 = "CREATE TABLE Ordercode(Ordercode VARCHAR(20),OrderNo VARCHAR(20),Cust_Name VARCHAR(20),Rest_Name VARCHAR(20))"
            #self.cursor.execute(self.q1)

            self.q2="INSERT INTO Ordercode(Ordercode,OrderNo,Cust_Name,Rest_Name) VALUES(%s,%s,%s,%s)"
            self.values=[self.ordercode,self.s7,self.s8,self.s9]
            self.cursor.execute(self.q2,self.values)
            self.db.commit()

            print("-------------------------------------------------------------")
            print("Pls Write 'Order display' to get the confirmation of order..")
            print("--------------------------------------------------------------")
            break



obj=Payment()