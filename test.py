
import pymysql.cursors
host="mysql-rfam-public.ebi.ac.uk"
user="rfamro"
password="none"
port=4497
database="Rfam"

# Connect to the database
connection = pymysql.connect(host=host,
                             port=port,
                             user=user,
                             password=None,
                             database=database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "select ncbi_id from taxonomy where LOWER( species )like '%oryza%sativa%';"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)