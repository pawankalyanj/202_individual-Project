from main import CONNECTION
from main import conn
if conn:
    # create sensor data hypertable
            query_create_sensordata_table = """CREATE TABLE sensor_data (
                                                ts TIMESTAMPTZ NOT NULL,
                                                sensor_id INTEGER,
                                                temp DOUBLE PRECISION,
                                                ext DOUBLE PRECISION,
                                                humidity DOUBLE PRECISION,
                                                );"""