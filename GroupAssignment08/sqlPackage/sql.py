# Name: Jared Turner
# email: turne2jw@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:03/28/2024
# Course/Section: IS4010-001
# Semester/Year: spring 2024
# Brief Description of the assignment:THis assignemnt executes a sql statement on a data base and retrives the information
# Brief Description of what this module does. This module prints the statement
# Citations: class
#https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python
#https://stackoverflow.com/questions/14835852/convert-sql-result-to-list-python
#https://flexiple.com/python/python-print-list
# Anything else that's relevant:

from groceryPackage.grocery import groceryData
class sqlQuery:
    '''
    Converts GroceryData to create a cursor 
    Executes SQL statement
    @return Print statement and Query in string format 
    '''
    
    sqlData = groceryData()
    sqlCursor = sqlData.connect('GroceryStoreSimulator')
    sqlCursor.execute(
            '''
            SELECT  Top 10   tProduct.ProductID, tBrand.BrandID, tBrand.Brand, tTransactionDetail.QtyOfProduct
            from tBrand
            inner join tProduct on tProduct.BrandID = tBrand.BrandID
            inner join tTransactionDetail on tProduct.ProductID = tTransactionDetail.ProductID
            order by tTransactionDetail.QtyOfProduct desc
            '''
            )
   
    brandsList = []

    for column in sqlCursor:
        # Append the brand name to the list
        brandsList.append(column[2])

    # Join the brand names into a single string, separated by commas and spaces
    brandString = ", ".join(brandsList)

    # Print the sentence
    print("Top 10 brands by product quantity: ", brandString)
        