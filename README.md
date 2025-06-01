---
title: "🍇 Blueberry Yield Regression"
emoji: 🌾
colorFrom: indigo
colorTo: green
sdk: streamlit
app_file: app.py
pinned: true
license: mit
tags:
  - regression
  - machine-learning
  - streamlit
  - kaggle
  - agriculture
---
https://huggingface.co/spaces/yazodi/blueberry-yield-regression-app/tree/main download model...
# 🍇 Blueberry Yield Prediction with Machine Learning

This project is a complete machine learning pipeline that predicts the **yield of wild blueberries** using various environmental and biological features such as pollinator counts, rainfall, and fruit measurements.

## 📌 Project Type

- Supervised Learning
- Regression Problem

---

## 🔍 Problem Description

Predicting agricultural yield is a crucial component in planning, sustainability, and food economics. The dataset used in this project comes from the **Kaggle Playground Series S3E14** competition and contains information on:

- Different species of pollinators (honeybee, bumblebee, osmia...)
- Environmental conditions (rainfall days, temperature ranges...)
- Fruit attributes (fruit mass, fruit set, seed count...)

🎯 **Goal**: Predict the `yield` (kg/ha) of blueberries based on input features.

---

## 📊 Dataset Info

- `train.csv`: 15,289 samples with 18 features
- `test.csv`: same structure, no target
- No missing values, clean numerical data

---

## 📈 What We Did (Pipeline Summary)

1. **EDA (Exploratory Data Analysis)**  
   - Checked for missing values ✅  
   - Analyzed feature distributions & target (`yield`)  
   - Built correlation heatmaps — strongest positive correlations:  
     - `fruitmass`, `fruitset`, `seeds`

2. **Data Preprocessing**  
   - Removed `id` column  
   - Standard feature selection based on correlation  
   - No categorical encoding needed (all numerical)

3. **Model Training**  
   - Model: `RandomForestRegressor`  
   - Train-Test Split: 80/20  
   - **Results**:  
     - RMSE ≈ **573.8**  
     - R² Score ≈ **0.81** ✅

4. **Test Prediction & Submission**  
   - Predictions made on `test.csv`  
   - `submission.csv` generated for Kaggle submission

5. **Streamlit App**  
   - Users input bee counts, rain days, and fruit measurements  
   - Predicts blueberry yield in kg/ha  
   - Uses trained model (`rf_model.pkl`) behind the scenes

---

## 🚀 Try it Online

🌐 You can try this app live here:  
[Hugging Face Space Link](https://huggingface.co/spaces/yazodi/blueberry-yield-regression-app)

---

## 🔮 What Could Be Improved?

| Area | Suggestion |
|------|------------|
| Feature Engineering | Create interaction terms, try log/ratio features |
| Model | Try LightGBM, XGBoost, or stacking |
| Tuning | GridSearchCV or Optuna for hyperparameter optimization |
| Visualization | Add interactive charts in Streamlit app |
| Real-World Data | Add satellite weather data, soil types, historical trends |

---

## 📁 Project Structure

📦 blueberry-yield-regression
├── app.py
├── rf_model.pkl
├── model_columns.pkl
├── requirements.txt
├── submission.csv
└── README.md


---

## 📜 License

MIT License – Free to use, modify and distribute.

---
