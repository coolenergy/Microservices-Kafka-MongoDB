import psycopg2

def select_all_cyberattacks():
    conn = psycopg2.connect(dbname='mydatabase', user='postgres', password='postgres', host='localhost:3011')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cyberattacks")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows