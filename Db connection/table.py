from main import CONNECTION
from main import conn
if conn:
        query_create_sensordata_hypertable = "SELECT create_hypertable('sensor_data', 'ts');"
        cursor = conn.cursor()
        cursor.execute(query_create_sensordata_hypertable)
        conn.commit()
        cursor.close()