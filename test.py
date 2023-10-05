import mysql
from mysql.connector import connect
host="mysql-rfam-public.ebi.ac.uk"
user="rfamro"
password="none"
port=4497
database="Rfam"
mydb=mysql.connector.connect(
    host=host,
    port=port,
    passwd=password,
    user=user,
    database=database
)