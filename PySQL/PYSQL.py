

import pypyodbc

SQLserver = "DESKTOP-MMDDPMA\SQLEXPRESS"
SQLDatabase = "AdventureWorks2017"
SQLconnect = pypyodbc.connect('driver={SQL server};'

                              'server=' + SQLserver + ';'

                              'Database=' + SQLDatabase + ' ;')

cursor = SQLconnect.cursor()


SQLQuery = ("""

SELECT addressline1
     
      [City]
      FROM [AdventureWorks2017].[Person].[Address]

""")

cursor.execute(SQLQuery)


results = cursor.fetchall()
print(results)


SQLconnect.close()