<h1> Overview of using pyodbc and Azure SQL Server with Docker </h1>
<br>
<h2> The Problem</h2>

- I faced an issue with connecting to an SQL database instance hosted on Azure from a Python script via pyodbc that was hosted on an Ubuntu docker container
  
<br>

<h2> The Cause </h2>

- The issue was caused by a few things:
  1.  The unixodbc driver manager was expecting the FreeTDS driver to exist in a specific directory but it was automatically installed elsewhere by the Dockerfile.
  2.  The connection string in the main.py script was not configured properly.

<br>

<h2> The Solution </h2>

1. The first issue was resolved by fixing the directory paths for the Driver and Setup variables within the configuration file (odbcinst.ini) setup section of the Dockerfile
2. The second issue was resolved by ensuring that the connection string contained each of the specific arguments.
    - The connection to the SQL database should be tested first with pyodbc alone, ensuring that pyodbc detects the appropriate drivers (in this case FreeTDS), then test the connection with SQLAlchemy

<br>

<h3> Link References </h3>

- [Python code for connecting to Azure SQL database via pyodbc and sqlalchemy](https://gist.github.com/eshirazi/e381fec4e9563d9088c4e642037bb4a5)
- [SQL Alchemy documentation for creating connection string](https://docs.sqlalchemy.org/en/14/dialects/mssql.html?highlight=azure#module-sqlalchemy.dialects.mssql.pyodbc)
- [Dockerize Python app that connects to external SQL server](https://towardsdatascience.com/deploying-python-script-to-docker-container-and-connect-to-external-sql-server-in-10-minutes-225ff4c19ce5)
  