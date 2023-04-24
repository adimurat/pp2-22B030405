import psycopg2

con = psycopg2.connect(host="localhost", database="gta", user="postgres", password="Aa12122004")
current = con.cursor()

current.execute('''CREATE TABLE mygame(name varchar, score varchar, level varchar);''')

current.close()
con.commit()
con.close()