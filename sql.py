import mysql.connector
import os
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='onlineretail1'  # Change this to your actual database name
)
cursor = connection.cursor()

# Read Excel file into a DataFrame
excel_file_path = 'C:\\Users\\bharg_m4sn0yd\\Downloads\\vpro\\project.xlsx'
df = pd.read_excel(excel_file_path)

# Iterate through rows and insert data into the table
for index, row in df.iterrows():
    # Modify this insert command based on the table structure and column names
    insert_query = '''
        INSERT INTO table1 (StockCode, Quantity, InvoiceDate, InvoiceTime, UnitPrice, CustomerID, Country)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    
    # Data to be inserted
    data = (
        row['StockCode'], row['Quantity'], row['InvoiceDate'], row['InvoiceTime'],
        row['UnitPrice'], row['CustomerID'], row['Country']
    )
    
    # Execute the insert command with parameterized values
    cursor.execute(insert_query, data)

# Commit changes and close the connection
connection.commit()
cursor.close()
connection.close()
