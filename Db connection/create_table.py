from main import CONNECTION
from main import conn
if conn:
    query_create_sensors_table = "CREATE TABLE sensors (id SERIAL PRIMARY KEY, type VARCHAR(50), location VARCHAR(50));"
    cursor = conn.cursor()
# see definition in Step 1
    cursor.execute(query_create_sensors_table)
    conn.commit()
    cursor.close()