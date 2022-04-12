import pyodbc
import sqlalchemy as sa
import urllib

print("App starting...")

server = "server_name"
port = "1433"
database = "database_name"
username = "username"
password = "password"
driver = "FreeTDS"

### CONNECT TO AZURE SQL DATABASE VIA PYODBC ###

# conn = pyodbc.connect(
#     "DRIVER={FreeTDS};SERVER=server_name;PORT=1433;DATABASE=database_name;UID=username;PWD=password", autocommit=True)
# cur = conn.cursor()
# cur.execute("SELECT @@VERSION AS 'SQL Server Version';")
# results = cur.fetchall()
# for row in results:
#     print(row)
# print(pyodbc.drivers())
# conn.commit()
# cur.close()
# conn.close()


### CONNECT TO AZURE SQL DATABASE WITH SQLALCHEMY VIA PYODBC ###

connection_string = "DRIVER={FreeTDS};SERVER={server_name};PORT=1433;DATABASE={database_name};UID={username};PWD={password};Port=1433;"
params = urllib.parse.quote_plus(connection_string)
engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
connection = engine.connect()
results = connection.execute("SELECT @@VERSION AS 'SQL Server Version';")
for row in results:
    print(row)

print("App end.")
