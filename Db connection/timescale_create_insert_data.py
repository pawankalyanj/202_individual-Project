import psycopg2

CONNECTION = "<repalce this>"
conn = psycopg2.connect(CONNECTION)

query_create_sensors_table = "CREATE TABLE sensors (id SERIAL PRIMARY KEY, type VARCHAR(50), location VARCHAR(50));"
cursor = conn.cursor()
# see definition in Step 1
cursor.execute(query_create_sensors_table)
conn.commit()
cursor.close()

# create sensor data hypertable
query_create_sensordata_table = """CREATE TABLE sensor_data (
                                           time TIMESTAMPTZ NOT NULL,
                                           sensor_id INTEGER,
                                           temperature DOUBLE PRECISION,
                                           cpu DOUBLE PRECISION,
                                           FOREIGN KEY (sensor_id) REFERENCES sensors (id)
                                           );"""

query_create_sensordata_hypertable = "SELECT create_hypertable('sensor_data', 'time');"

# create conn
cursor = conn.cursor()
cursor.execute(query_create_sensordata_table)
cursor.execute(query_create_sensordata_hypertable)
# commit changes to the database to make changes persistent
conn.commit()
cursor.close()



#Insert data

from pgcopy import CopyManager
mgr = CopyManager(conn, 'sensor_data', cols)
mgr.copy(values)

conn.commit()

# insert using pgcopy
cursor = conn.cursor()

# for sensors with ids 1-4
for id in range(1, 4, 1):
    data = (id,)
    # create random data
    simulate_query = """SELECT generate_series(now() - interval '24 hour', now(), interval '5 minute') AS time,
                        %s as sensor_id,
                        random()*100 AS temperature,
                        random() AS cpu
                    """
    cursor.execute(simulate_query, data)
    values = cursor.fetchall()

    # column names of the table you're inserting into
    cols = ['time', 'sensor_id', 'temperature', 'cpu']

    # create copy manager with the target table and insert
    mgr = CopyManager(conn, 'sensor_data', cols)
    mgr.copy(values)

# commit after all sensor data is inserted
# could also commit after each sensor insert is done
conn.commit()


#view data
cursor = conn.cursor()
query = "SELECT * FROM sensor_data;"
cursor.execute(query)
for row in cursor.fetchall():
    print(row)
cursor.close()
