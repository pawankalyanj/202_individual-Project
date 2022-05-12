import psycopg2

CONNECTION = "postgres://tsdbadmin:AVNS_qdv_vgOhhiXe9T2@tsdb-206531ac-sjsu-0c73.a.timescaledb.io:16433/sensordata?sslmode=require"
conn = psycopg2.connect(CONNECTION)

def hello_world(request):
    request_json = request.get_json()
    if request_json and 'ts' in request_json:
        now_utc = request_json['ts']
        temp = request_json['temp']
        ext = request_json['ext']
        humidity = request_json['humidity']
        sensor_type = request_json['sensor_type']
        sensor_location = request_json['sensor_location']
        sensor_id = request_json['sensor_id']

        isAnomalyTemp = 0
        isAnomalyHumidity = 0
        anomalyType = []
        
        temp_mean = 25.165
        tsd = 3.1120
        
        if ((temp > temp_mean-1*tsd) and (temp < temp_mean+1*tsd)):
            isAnomalyTemp = 0

        if ((temp > temp_mean+2*tsd) or (temp < temp_mean-2*tsd)):
            isAnomalyTemp =  1

        if ((temp > temp_mean+3*tsd) or (temp < temp_mean-3*tsd)):
            isAnomalyTemp = 2

        cursor = conn.cursor()
        cursor.execute("INSERT INTO hvac_data_live (time, sensor_id, sensor_type, sensor_location, temp, ext, humidity, is_anomaly_temp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (now_utc, sensor_id, sensor_type, sensor_location, temp, ext, humidity, isAnomalyTemp))
        conn.commit()

        print("Values", now_utc, temp, ext, humidity)
        return "Success"
    else:
        return f'No params passed'
