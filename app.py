import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Başlık
st.title("🍇 Blueberry Yield Prediction App")
st.write("Bu uygulama, çevresel ve biyolojik faktörlere göre yaban mersini verimini tahmin eder.")

# Giriş alanları
clonesize = st.slider("Klon Boyutu", 0.0, 10.0, 1.0)
honeybee = st.slider("Bal Arısı Sayısı", 0.0, 10.0, 1.0)
bumbles = st.slider("Bumblebee Sayısı", 0.0, 10.0, 1.0)
andrena = st.slider("Andrena Sayısı", 0.0, 10.0, 1.0)
osmia = st.slider("Osmia Sayısı", 0.0, 10.0, 1.0)
RainingDays = st.slider("Yağmurlu Günler", 0.0, 100.0, 20.0)
AverageRainingDays = st.slider("Ortalama Yağmurlu Günler", 0.0, 100.0, 30.0)
fruitset = st.slider("Fruit Set", 0.0, 1.0, 0.5)
fruitmass = st.slider("Fruit Mass", 0.0, 10.0, 5.0)
seeds = st.slider("Tohum Sayısı", 0.0, 100.0, 50.0)

# DataFrame'e dönüştür
user_input = pd.DataFrame([{
    "clonesize": clonesize,
    "honeybee": honeybee,
    "bumbles": bumbles,
    "andrena": andrena,
    "osmia": osmia,
    "RainingDays": RainingDays,
    "AverageRainingDays": AverageRainingDays,
    "fruitset": fruitset,
    "fruitmass": fruitmass,
    "seeds": seeds
}])

# Model ve sütunlar yükleniyor
model = joblib.load("rf_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# Eksik sütunları ekle
for col in model_columns:
    if col not in user_input.columns:
        user_input[col] = 0

user_input = user_input[model_columns]

# Tahmin
if st.button("Tahmini Göster"):
    pred = model.predict(user_input)[0]
    st.success(f"🌱 Tahmini Yaban Mersini Verimi: {pred:.2f} kg/ha")
