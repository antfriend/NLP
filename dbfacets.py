#get newly indexed facet values from DB

import pyodbc as p

server = 'hw-cde-ddb01'
database = 'Crowded'
table = 'INDEXER_ANSWER'
field = 'content_id'
field2 = 'facet'

connStr = (r'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';' + 'UID=CrowdApp;PWD=CrowdApp' )
conn = p.connect(connStr)

sql = ('select * from db_accessadmin.INDEXER_ANSWER')

dbCursor = conn.cursor()
print 'connected to db'
dbCursor.execute(sql)
print '======ROWS======='
for row in dbCursor:
    print row
    
