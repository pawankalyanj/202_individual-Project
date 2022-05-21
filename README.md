# Group-25
## Project
### Title:
HVAC AnoML - A HVAC Anomaly Detection System 

### Problem statement:
Perform anomaly detection on time-series data of Internet of Things (IoT) based on Heating, Ventilation and Air Conditioning (HVAC) systems. HVAC systems are crucial in providing appropriate environmental conditions in terms of temperature, humidity, pressure, and flow rate while being energy efficient. With the rapid growth of IoT based HVAC systems it becomes crutial to detect short-term anomalies and long-term anomalies in heating and cooling, and air quality. The detection must be made in real-time/as soon as possible in in Hospitals, Data Centers, BioTech Labs. This becomes more challenging with large amounts of data. 

### Abstract:
To solve this, we are building a system to scalibily ingest HVAC IoT data and perform anomaly detection on it. 
This will cover
1. Ingest large volumes of data and store efficiently 
2. Analyse historical data and build ML models based off of them
3. Perform real-time/ near real time analysis on the incoming streaming data

### Approach:
Our basic approach is that the data from the sensors gets ingested into the cloud via GCP Functions.  The system was tested with bursty high-velocity data like seen on some sensors - the serverless functions were able to autoscaling upto 100 to support high velocity ingestion and scaling down. There are two parts of the system, detection of real-time anomalies and prediction of future breakdowns. For real-time, we use an algorithm that learns the pattern from the data and detects real-time anomaly using Z-Score (with millisecond latency). While for predictions, we used a RNN based model leveraged via Facebook's Prophet software.

Basic Architecture 
![arcg](https://user-images.githubusercontent.com/32498849/169204892-97a6a866-74cc-403c-bc88-8c1ee1c8d755.gif)

### Relevant Dataset:
https://ieee-dataport.org/documents/hvac-air-handling-units-one-year-data-medium-large-size-academic-building

--
### Example program dashboard
<img width="987" alt="Screen Shot 2022-05-18 at 9 23 12 PM" src="https://user-images.githubusercontent.com/32498849/169204220-341282a8-9ad2-42e8-9abd-b618ed69d3aa.png">

---

### Understanding and researching users and personas for our application
#### Personas 
HVAC Technician

WANTS
- A quick tool/application that can notify of any energy usage out of the ordinary 
- Perform cursory check on HVAC systems before enlisting more complicated tools and applications 

FRUSTRATIONS
- There are no applications that perform a birds eye view analysis of the HVAC systems and their output
- Time series meta data of an HVAC system is harde to parse through to perform quick analysis


Business Owner 

WANTS
- Wants to be able to ensure HVAC machines are working to the best of their capacity
- Wants to be able to focus on business matters than be bogged down by routine checks of HVAC systems that maybe crucial to running of business 
- Smarter solutions that don’t require technical or programming expertise to enlist the latest advancements in data crunching technologies

FRUSTRATIONS
- Does not have the technical knowledge to perform cursory checks on efficiency of HVAC Machines
- Does not have the appropriate equipment or sensors to perform checks on HVAC Systems
- Does not have the appropriate knowledge to parse through metadata provided by IoT based apps

### Empathy map 
![EMPATHY MAP 272](https://user-images.githubusercontent.com/32498849/162877126-24067b58-aec2-4ecd-aab1-eae6b073f6ae.png)

### AS-IS and To-Be scenarios
#### **Problem Statement**

Improve the energy efficiency of HVAC systems - that can scale and perform data-driven analysis.

#### **Gap Identification**

Field surveys have shown that 60 percent of HVAC systems are operating below the manufacturer's specifications. Deviation from manufacturer's specifications can mean a large increase in energy consumption.

This impacts people in the residence to keep their units operating at peak efficiency, or HAVCs in Labs where missing an issue can lead to fatalities. Having alerts on anomalies and actionable insights can help save energy and prevent fatalities from occurring.

HVACAnomaly will fill the gap of alerting technicians in a timely manner and managers with actionable dashboards. HVACAnomaly also takes into account the rapid growth rate of HVACs by designing it to be a scalable monitoring system.



#### **Root cause Analysis** 

Some common issues faced are:

- Unnecessary Maintenance Call 
If the coolant levels are correct, the filters are clean, and there are no other problems, the maintenance call may not have been necessary. This results in unnecessary expense and inconvenience for the homeowner.
- Missing a probable issue
- A leak may develop and/or a component may malfunction and the problem may not be noticed by the homeowner and, therefore, not corrected until the next scheduled tune-up. This could result in ever-increasing utility bills for the homeowner, and it could result in permanent damage to the HVAC system.
- Scalable System 
With the fast growth rate, one needs a system that scales along.

#### **Improvement Plan**

- Timely real-time alerts with reduced false positives
- HVACAnomaly will alert technicians in a timely manner and reduce the unwanted false alerts 
- Run batch jobs every day that performs routine analysis of HVACs. This data will be displayed for Managers with actionable dashboards. 
- Build to scale, current systems use MySql databases with schemas that need to be predefined. HAVCAnomaly will be built ground-up to be a scalable monitoring system.


#### **Solution Statement**

HVACAnomaly is an intelligent alerting system providing actionable dashboards. It is a scalable HVAC monitoring system.

###  Hills/sub-hills that capture the theme of the problem we are solving
#### Who
Who are your users? Make it clear who you aim to serve—and who you don’t.
Our aim is to serve small and large businesses and commercial and residential buildings. The large enterprises with data centers, multi-story commercial buildings, and people with individual houses are our customers. And on the other hand, there is no point in installing air conditioning for a customer residing in Canada and installing a heating system for a commercial building in UAE. For now, let’s say these are  “The not so great areas”. So we need to adapt our business model according to local climatic conditions

#### What
What’s the need they’re trying to meet? Turn user needs into project goals.
According to IBM In 2020, 59% of the electricity consumed by IBM globally came from renewable sources and they are aiming to make it 90% by 2030. This is a budget and eco-friendly solution.
As a business owner, anyone will try to cut down the installation and maintenance costs, for example, the data center running with 100’s of machines needs to be cooled down and keep the temperature in check for efficient performance. In this situation we don’t need to invest a lot in heating solutions. So meeting the customer’s needs and demands by offering the best cost-efficient method will write a great success story.
 
#### How
How will you differentiate from competitors? How will you measure success?
We are offering the best cost-efficient and eco-friendly solution according to their business and individual needs. This can be achieved by using renewable energy and biofuels and also implementing an HVAC system according to local climate conditions and which best suits their own needs. This will gradually cut down the cost for any business or an individual. As we discussed earlier, adapting to climate change and using renewable energy sources for an efficient solution is the key to our success.

---
