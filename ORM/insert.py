import psycopg2

def insert_builk_cyberattacks(data):
    conn = psycopg2.connect(dbname='mydatabase', user='postgres', password='postgres', host='localhost:3011')
    cursor = conn.cursor()

    for item  in data:
        cursor.execute("INSERT INTO cyberattacks (name, type, description) VALUES (%s, %s, %s)", (item['name'], item['description'], item['description']))
    conn.commit()
    print(f"We have saved {len(data)} items into Postgres")
    cursor.close()
    conn.close()