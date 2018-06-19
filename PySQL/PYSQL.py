

import pypyodbc

SQLserver="DESKTOP-MMDDPMA\SQLEXPRESS"
SQLDatabase="AdventureWorks2017"
SQLconnect = pypyodbc.connect('driver={SQL server};'

                              'server='+ SQLserver + ';'

                              'Database=' + SQLDatabase + ' ;')

cursor = connection.cursor()


SQLQuery = ("""

SELECT TOP (1000) [AddressID]
      ,[AddressLine1]
      ,[AddressLine2]
      ,[City]
      ,[StateProvinceID]
      ,[PostalCode]
      ,[SpatialLocation]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2017].[Person].[Address]

""""")

cursor.execute(SQLQuery)

results = cursor.fetchall()

