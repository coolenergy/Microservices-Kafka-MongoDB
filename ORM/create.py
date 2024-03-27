import psycopg2

def create_cyberattacks():
    conn = psycopg2.connect(dbname='mydatabase', user='postgres', password='postgres', host='localhost:3011')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE cyberattacks (id SERIAL PRIMARY KEY, name VARCHAR(255), type VARCHAR(255), description TEXT)")

    conn.commit()

    cursor.close()
    conn.close()
