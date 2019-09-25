import os
import sys
import  mysql.connector

class find_orderitems:
    def Read_file(self):
        self.db=mysql.connector.connect(host="localhost",user="root",passwd="user123",database="MENU")
        self.cursor=self.db.cursor()

        self.t1=input("Enter OrderNo:")

        self.q1="SELECT OrderNo FROM orderplaced"   # all orderno from orderplaced table...
        self.cursor.execute(self.q1)
        self.data=self.cursor.fetchall()
        #print(self.data)

        self.order=list(filter(lambda l1:(self.t1 in l1),self.data))   # check entered orderNo is present or not..
        #print(self.order)    # tuple in list eg. [('order1',)]

        if(len(self.order)==0):
            print("Order doesn't Exist...")
        else:
            self.s1=""
            for var in self.order:
                self.s1=''.join(var[0])   # convert tuple in string(orderno-table name)...
                #print("s1:",self.s1)


            self.q2="SELECT * FROM "+self.s1
            self.cursor.execute(self.q2)
            self.data2=self.cursor.fetchall()
            #print(self.data2)
            print("ItemName" + "    " + "Quantity" + "   " + "price")
            print("---------------------------")
            self.l1=list()
            for item in self.data2:
                self.s2=''.join(item[0:1])     # convert tuple in string..
                self.s3=''.join(item[1:2])
                self.s4=''.join(item[2:])
                self.l1.append(self.s2)         # append all items in list...

                print(self.s2+"     "+self.s3+"            "+self.s4)

            self.q3="SELECT name FROM dessert "
            self.cursor.execute(self.q3)
            self.data3=self.cursor.fetchall()


            self.s1=[''.join(items[0:1]) for items in self.data3]   # list comprehension for dessert name...

            #print(self.s1)


            self.sweet=[sweet   for sweet in self.l1   if(sweet in self.s1) ]  # list comprehension if order contains Dessert or not...

            if(len(self.sweet)==0):
                print()
                print("order doesn't contain Dessert....")
            else:
                print()
                print("Order contains Dessert:", self.sweet)




obj=find_orderitems()
obj.Read_file()