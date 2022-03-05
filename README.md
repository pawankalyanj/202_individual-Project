# Group-25
## Project
### Title:
HVAC Anomaly Detection System 

### Problem statement:
Many problems around us deal with understanding patterns and recognizing anomalies *in realtime*. For example, the task of monitoring a datacentermight include CPU usage for various servers, bandwidth measurements, latency of servicing requests, etc. At each point in time t we would like to determine whether the behavior of the system is unusual. The determination must be made in real-time/as soon as possible. This becomes more challenging with large amounts of data. 

### Abstract:

To solve this, we are building a system to scalibily ingest IoT data and perform anomaly detection on it. 
This will cover
1. Ingest large volumes of data and store efficiently 
2. Analyse hostorical data and build ML models on them
3. Perform real-time/ near real time analysis on the incoming streaming data

### Approach:

Basic Architecture 
![ai basic anomaly project](https://user-images.githubusercontent.com/98665151/155423222-68623b06-e9a8-4691-98bf-979baf453cc4.jpeg)

### Personas:
Manufacturing Shop Floor monitor, Data Centers Monitoring, Any Critical Monitoring systems/ workforce

### Relevant Datasets:
https://github.com/sassoftware/iot-anomaly-detection-hvac/tree/master/data

https://catalog.data.gov/dataset/alphabuilding-synthetic-dataset

https://ieee-dataport.org/documents/hvac-air-handling-units-one-year-data-medium-large-size-academic-building

