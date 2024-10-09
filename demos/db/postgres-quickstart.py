import psycopg2

conn = psycopg2.connect(database = "dev",
                        user = "cbq",
                        host= 'localhost',
                        password = "cbq1024",
                        port = 5432)
cur = conn.cursor()
cur.execute('SELECT * FROM db."user"')
rows = cur.fetchall()
conn.commit()
conn.close()
for row in rows:
    print(row)