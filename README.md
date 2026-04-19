# Monthly Sales Forecasting using Regression and Time Features

## Project Overview
This project focuses on forecasting monthly sales using regression models with engineered time-based and seasonal features.

The model incorporates seasonality, temperature data, and time trends to improve prediction quality.

---

## Goal
To predict monthly sales volume and analyze how seasonal patterns and external factors (such as temperature) influence demand.

---

## Data Description

The dataset includes:
- Monthly sales volume (historical data)
- Date information (year, month)
- External temperature data
- Seasonal indicators

Additional engineered features:
- Seasonal indicator (summer months)
- Cyclical encoding (sin/cos of month)
- Time index (trend component)

---

## Methodology

The project follows these steps:

- Data loading from Excel
- Data preprocessing and aggregation by month
- Feature engineering:
  - seasonal encoding (sin/cos)
  - summer indicator
  - time index
- Merging with temperature data
- Model training using Linear Regression
- Future forecasting (2023–2024)
- Visualization of actual vs predicted values

---

## Model

- Linear Regression (scikit-learn)

Input features:
- Season indicator
- sin(month)
- cos(month)
- Temperature
- Time index

---

## Evaluation

- R² score used for model quality assessment
- Visual comparison of actual vs predicted values

---

## Key Insights

- Sales demonstrate strong seasonal patterns
- Cyclical encoding improves model performance
- Temperature has a noticeable influence on demand
- Time trend helps capture long-term growth/decline

---

## Forecast

The model is used to predict sales for:
- Remaining months of 2023
- Full year 2024

---

## Tech Stack

- Python  
- pandas  
- numpy  
- scikit-learn  
- matplotlib  

---

## Key Takeaway
Incorporating time-based and seasonal features significantly improves regression performance in sales forecasting tasks.
