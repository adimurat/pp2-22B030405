import psycopg2

con = psycopg2.connect(host="localhost", database="mybook", user="postgres", password="Aa12122004")
current = con.cursor()

current.execute('''CREATE TABLE phone(name varchar, number varchar);''')

current.close()
con.commit()
con.close()