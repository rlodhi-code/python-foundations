# 🌦️ Weather & Squirrel Data Analysis  
A beginner‑friendly data processing project using **pandas** to explore weather data and analyze NYC squirrel census data. This project demonstrates how to read CSV files, perform basic data analysis, filter rows, compute statistics, and generate new datasets.

---

## 📌 Project Overview
This folder contains two small data‑analysis exercises:

### **1. Weather Data Exploration**
Using `weather_data.csv`, the script demonstrates:
- Reading CSV files with pandas  
- Converting columns to lists  
- Computing summary statistics (e.g., mean temperature)  
- Selecting rows based on conditions  
- Accessing specific values (e.g., Monday’s temperature)  

### **2. NYC Squirrel Census Analysis**
Using `squirrel_data.csv`, the script:
- Reads a large dataset of squirrel observations  
- Counts squirrels by primary fur color  
- Creates a summary table  
- Exports the results to `squirrel_count.csv`  

This mirrors a common real‑world workflow: load → clean → analyze → export.

---

## 🗂️ Folder Contents

| File | Description |
|------|-------------|
| `main.py` | Main analysis script demonstrating CSV reading, filtering, and aggregation. |
| `weather_data.csv` | Small dataset of daily temperatures and weather conditions. |
| `squirrel_data.csv` | Large dataset from the NYC Squirrel Census (sample shown below). |
| `squirrel_count.csv` | Output file summarizing squirrel counts by fur color. |

---

## 📄 Dataset Details

### **weather_data.csv**
A simple dataset used to practice reading and analyzing tabular data.

```
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny
```

### **squirrel_data.csv** (sample)
The real file contains **3,000+ rows**. Here is a small excerpt:

```
X,Y,Unique Squirrel ID,Hectare,Shift,Date,Hectare Squirrel Number,Age,Primary Fur Color,...
-73.95613449,40.79408239,37F-PM-1014-03,37F,PM,10142018,3,,,+,...
-73.96885747,40.78378252,21B-AM-1019-04,21B,AM,10192018,4,,,+,...
-73.97428115,40.77553362,11B-PM-1014-08,11B,PM,10142018,8,,Gray,,Gray+,...
```

---

## 📥 Data Source (NYC Squirrel Census)

The squirrel dataset used in this project comes from the **2018 Central Park Squirrel Census**, published on **NYC Open Data**:

**NYC Open Data – 2018 Central Park Squirrel Census**  
`https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw` [(data.cityofnewyork.us in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fdata.cityofnewyork.us%2FEnvironment%2F2018-Central-Park-Squirrel-Census-Squirrel-Data%2Fvfnx-vebw")

This is the official, publicly available dataset containing:
- Geographic coordinates  
- Fur color  
- Behaviors  
- Age  
- Location notes  
- Observation metadata  

It is the same dataset used in many Python data‑analysis tutorials and courses.

---

## 🧪 What the Script Does

### **Weather Analysis Section**
The script demonstrates:

- Reading CSV data:
  ```python
  data = pandas.read_csv("weather_data.csv")
  ```

- Converting a column to a list:
  ```python
  temp_list = data["temp"].values.tolist()
  ```

- Computing the average temperature:
  ```python
  data["temp"].mean()
  ```

- Filtering rows:
  ```python
  data[data.day == "Monday"]
  data[data.temp == data.temp.max()]
  ```

### **Squirrel Census Analysis Section**
Counts squirrels by fur color:

```python
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
```

Creates a summary DataFrame:

```python
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
```

### **Output Example (`squirrel_count.csv`)**
```
Fur Color,Count
Gray,2473
Cinnamon,392
Black,103
```

---

## ▶️ Running the Project

### **Requirements**
- Python 3.x  
- `pandas`  

Install pandas:

```bash
pip install pandas
```

### **Run the script**
```bash
python main.py
```

The script will print squirrel counts to the console and generate `squirrel_count.csv`.

---

## 🎯 Learning Objectives

This project reinforces core data‑processing skills:

- Reading CSV files with pandas  
- Converting columns to lists  
- Filtering and selecting data  
- Computing summary statistics  
- Creating and exporting DataFrames  
- Working with large datasets  

These are foundational skills for anyone learning data analysis or preparing for more advanced topics like data cleaning, visualization, or machine learning.

---

