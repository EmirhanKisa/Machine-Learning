# Ebebeyinli kod
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("student_data.csv")

df.drop(columns=[
    "Dalc", "Walc", "health", "absences", "goout", "freetime", "famrel",
    "romantic", "internet", "higher", "nursery", "activities", "paid",
    "famsup", "schoolsup", "failures", "traveltime", "guardian", "reason",
    "address", "school", "sex", "age", "famsize", "Pstatus"
], inplace=True)

df = pd.get_dummies(df, columns=["Mjob", "Fjob"], drop_first=True)

X = df[["studytime", "Medu", "Fedu", "G1", "G2"] +
       [col for col in df.columns if "Mjob_" in col or "Fjob_" in col]]
y = df["G3"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Tahmin yap
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)  # Aynı şey: r2_score(y_test, y_pred)

# Çıktı
print(f"Ortalama Kare Hata (MSE): {mse:.2f}")
print(f"Modelin R^2 doğruluk skoru: {r2:.4f}")
print(f"accuracy = {r2*100:.2f}")  # yüzde olarak
print(f"\nBu model, test verisi üzerinde yaklaşık %{r2*100:.2f} doğruluk sağlamaktadır.")
