import os
import sys
import mysql.connector

class find_payment_type:
    def Read_file(self):
        self.db = mysql.connector.connect(host="localhost", user="root", passwd="user123", database="MENU")
        self.cursor = self.db.cursor()

        self.t1 = input("Enter OrderNo : ")

        self.q1 = "SELECT OrderNo FROM orderplaced"  # all orderno from orderplaced table...
        self.cursor.execute(self.q1)
        self.data = self.cursor.fetchall()
        # print(self.data)

        self.order = list(filter(lambda l1: (self.t1 in l1), self.data))  # check entered orderNo is present or not..
        # print(self.order)    # tuple in list eg. [('order1',)]

        if (len(self.order) == 0):
            print("Order doesn't Exist...")
        else:
            self.s1 = ""
            for var in self.order:
                self.s1 = ''.join(var[0])  # convert tuple in string(orderno-table name)...
                # print("s1:",self.s1)
                self.q2="SELECT Ordercode,OrderNo FROM ordercode"
                self.cursor.execute(self.q2)
                self.data2=self.cursor.fetchall()

                #print(self.data2)  # [('6789','order2'),('1234','order3')]
                self.code=[''.join(var[0]) for var in self.data2 if (self.s1 in var)]  # list comprehension for ordercode..eg. for order2=['6789']
                #print(self.code)
                print()

                for code in self.code:

                    if(code=='1234'):
                        print("Order done by Paytm...")
                    elif(code=='4567'):
                        print("Order done by Netbanking...")
                    elif(code=='6789'):
                        print("Order done by Card...")


obj=find_payment_type()
obj.Read_file()