import os
import sys
import mysql.connector

class find_owner:
    def Read_file(self):
        self.db=mysql.connector.connect(host="localhost",user="root", passwd="user123", database="MENU")
        self.cursor=self.db.cursor()

        self.q1="SELECT OrderNo,Cust_Name FROM orderplaced"
        self.cursor.execute(self.q1)
        self.data=self.cursor.fetchall()
        print(self.data)   # print list of all order and cust_name in tuple form.eg.[('order1','Avani'),('order2','Kuman')]

        self.Avani=[self.var[0] for self.var in self.data if 'Avani' in self.var]   # list comprehension for cust_name='Avani'
        print("Avani's Order: ", self.Avani)

        self.Kuman=[self.var[0] for self.var in self.data if 'Kuman' in self.var]   #list comprehension for cust_name='Kuman'
        print("Kuman's Order: ", self.Kuman)

        self.Ruchi=list(filter(lambda data1:('Ruchi' in data1),self.data))   # lambda and filter function for cust_name='Ruchi'
        print("Ruchi's Order: ",self.Ruchi)

        self.db.commit()

obj=find_owner()
obj.Read_file()

