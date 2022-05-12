import psycopg2
from datetime import datetime, timedelta

CONNECTION = "postgres://tsdbadmin:AVNS_qdv_vgOhhiXe9T2@tsdb-206531ac-sjsu-0c73.a.timescaledb.io:16433/sensordata?sslmode=require"
conn = psycopg2.connect(CONNECTION)

def prediction(request):
  cursor = conn.cursor()
  d = (datetime.today() - timedelta(days=370)).strftime('%Y-%m-%d %H:%M:%S')
  preds = []
  for sensor_id in ['sensor_1', 'sensor_2', 'sensor_3', 'sensor_4', 'sensor_5', 'sensor_6', '1001']:
    query = f"SELECT time, temp, sensor_location FROM hvac_data WHERE time > '{d}' AND sensor_id='{sensor_id}';"
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall(), columns=['ds', 'y'])
    df.ds = pd.to_datetime(df.ds).dt.tz_localize(None)
    from prophet import Prophet
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=1)
    print(future.tail())
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    temp_mean = 25.165
    tsd = 3.1120
    
    prediction = "Normal"
    if (forecast[forecast['yhat'] > temp_mean+tsd].shape[0] > 0):
      prediction = "There is a increasing trend, potential breach"
    if(forecast[forecast['yhat'] < temp_mean-tsd].shape[0] > 0):
      prediction = "There is a decreasing trend, potential breach"
    if (forecast[forecast['yhat'] > temp_mean+2*tsd].shape[0] > 0):
      prediction = "Amber Alert: There is a increasing trend, high possibility of a breach"
    if(forecast[forecast['yhat'] < temp_mean-2*tsd].shape[0] > 0):
      prediction = "Amber Alert: There is a decreasing trend, high possibility of a breach"
    if (forecast[forecast['yhat'] > temp_mean+3*tsd].shape[0] > 0):
      prediction = "Red Alert: Fix required"
    if(forecast[forecast['yhat'] < temp_mean-3*tsd].shape[0] > 0):
      prediction = "Red Alert: Fix required"    
    preds.append([(datetime.today()).strftime('%Y-%m-%d %H:%M:%S'), sensor_id, prediction])
    cursor.execute("INSERT INTO hvac_data_prediction (time, sensor_id, prediction) VALUES (%s, %s, %s);", ((datetime.today()).strftime('%Y-%m-%d %H:%M:%S'), sensor_id, prediction))
    conn.commit()
  return preds
