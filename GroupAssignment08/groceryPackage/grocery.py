#Grocery.py
# Name: Jake Elmore
# email: Elmorejc@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: March 27 2024
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Connect 3 tables 

# Brief Description of what this module does. Connect to the database
# Citations: in class
# Anything else that's relevant:

import pyodbc

class groceryData:
    '''
    Connect to the grocery store simulator data base
    @return cursor
    '''
    def connect(self, database = "GroceryStoreSimulator"):
       
        conn = pyodbc.connect('Driver={SQL Server};'
                             'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                             'Database=' +
                            "GroceryStoreSimulator"';'
                            'uid=IS4010Login;'
                            'pwd=P@ssword2;')
        cursor = conn.cursor()
        return cursor 
